from django.db import models
from ckeditor.fields import RichTextField


class Class(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    class_name = models.ForeignKey(to=Class, on_delete=models.CASCADE)
    theme = models.CharField(max_length=200)
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
