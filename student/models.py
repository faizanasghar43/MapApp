from django.contrib.auth.models import AbstractUser
from django.db import models

class Student(AbstractUser):
    """Extend the User model for students and other users"""
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        """return email of user"""
        return self.email

    def get_name(self):
        """return name of user"""
        return self.name

    def save(self, *args, **kwargs):
        # Generate a username by combining name and roll_number
        if not self.username:
            self.username = f"{self.name}_{self.roll_number}"

        super(Student, self).save(*args, **kwargs)
