from django.contrib import admin

from .models import Class, Lesson, Homework, Comment

admin.site.register(Class)
admin.site.register(Lesson)
admin.site.register(Homework)
admin.site.register(Comment)
