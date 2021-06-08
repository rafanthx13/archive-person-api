from person.models import News
from django.contrib import admin

from .models import Person, News, Tag

# Register your models to access in admin GUI.
admin.site.register(Person)
admin.site.register(News)
admin.site.register(Tag)