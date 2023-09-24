from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Student
User = get_user_model()
# Register your models here.
admin.site.register(Student) 
admin.site.register(User) 