from django.contrib import admin
from .models import Poem, Tag, Appreciation

# Register your models here.
admin.site.register(Poem)
admin.site.register(Tag)
admin.site.register(Appreciation)

