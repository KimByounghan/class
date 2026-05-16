from django import forms
from .models import UserEntry


class UserEntryForm(forms.ModelForm):
    class Meta:
        model = UserEntry
        fields = ["title", "content"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "제목"}),
            "content": forms.Textarea(attrs={"rows": 4, "placeholder": "내용을 입력하세요."}),
        }
