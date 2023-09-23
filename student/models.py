from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    """
    Custom User model with timestamped fields.
    """
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Student(User):
    """Extend the User model for students and other users."""
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        """Return email of user."""
        return self.email

    def get_name(self):
        """Return name of user."""
        return self.name

    

# class Student(AbstractUser):
#     """Extend the User model for students and other users"""
#     email = models.EmailField(unique=True)
#     name = models.CharField(max_length=100)
#     roll_number = models.CharField(max_length=10, unique=True)

#     def __str__(self):
#         """return email of user"""
#         return self.email

#     def get_name(self):
#         """return name of user"""
#         return self.name

#     def save(self, *args, **kwargs):
#         # Generate a username by combining name and roll_number
#         if not self.username:
#             self.username = f"{self.name}_{self.roll_number}"

#         super(Student, self).save(*args, **kwargs)
