from django.db import models
from ckeditor.fields import RichTextField

from django.conf import settings


class Class(models.Model):
    teacher = models.ForeignKey(to=settings.AUTH_USER_MODEL, limit_choices_to={"role": "teacher"}, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class_name = models.ForeignKey(to=Class, on_delete=models.CASCADE)
    theme = models.CharField(max_length=200)
    description = RichTextField(null=True)
    lesson_date = models.DateTimeField()

    def __str__(self):
        return f"{self.class_name.name} - {self.theme} - {self.lesson_date}"


class Homework(models.Model):
    lesson = models.OneToOneField(to=Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = RichTextField()
    file = models.FileField(upload_to="homeworks/", null=True, blank=True)

    def __str__(self):
        return self.title
