from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError


class CustomUserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        if not email:
            raise ValidationError("Users must have email address")
        if not first_name:
            raise ValidationError("Users must have first name")
        if not last_name:
            raise ValidationError("Users must have last name")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role="student",
        )
        user.set_password(raw_password=password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        user = self.create_user(email, first_name, last_name, password)
        user.is_superuser = True
        user.is_staff = True
        user.role = "teacher"
        user.save(using=self._db)
        return user
