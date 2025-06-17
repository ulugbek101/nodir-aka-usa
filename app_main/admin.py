from django.contrib import admin

from .models import Class, Lesson, Homework

admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Homework)
