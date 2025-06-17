from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField

from app_main.models import Class
from .managers import CustomUserManager
from django.contrib.auth.models import UserManager


class TeacherManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="teacher")


class StudentManager(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(role="student")


class CustomUserModel(AbstractBaseUser, PermissionsMixin):
    USER_ROLES = [
        ["teacher", "Teacher"],
        ["student", "Student"],
    ]

    email = models.EmailField(max_length=100, verbose_name="Email address", unique=True)
    first_name = models.CharField(max_length=100, verbose_name="First name")
    last_name = models.CharField(max_length=100, verbose_name="Last name")
    middle_name = models.CharField(max_length=100, verbose_name="Middle name", null=True, blank=True)
    address = models.CharField(max_length=100, verbose_name="Address", null=True, blank=True)
    phone_number = PhoneNumberField(verbose_name="Phone number", null=True, blank=True)

    role = models.CharField(choices=USER_ROLES, max_length=10, default="student")

    classes = models.ManyToManyField(to=Class)

    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Teacher(CustomUserModel):
    objects = TeacherManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = "teacher"
        super().save(*args, **kwargs)


class Student(CustomUserModel):
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        self.role = "student"
        super().save(*args, **kwargs)
