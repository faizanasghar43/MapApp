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

class Student(models.Model):
    """Extend the User model for students and other users."""
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        """Return email of user."""
        return self.user.email

    def get_name(self):
        """Return name of user."""
        return self.name
