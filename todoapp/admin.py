
from django.contrib import admin
from .models import TodoItem, Tag

admin.site.register(TodoItem)
admin.site.register(Tag)
