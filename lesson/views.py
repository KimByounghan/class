from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserEntryForm
from .models import UserEntry


@login_required
def home(request):
    if request.method == "POST":
        form = UserEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            return redirect("home")
    else:
        form = UserEntryForm()

    entries = UserEntry.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "lesson/home.html", {"form": form, "entries": entries})
