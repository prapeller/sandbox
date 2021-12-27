from django.contrib import admin

from todo.models import Todo, Project

admin.site.register(Todo)
admin.site.register(Project)