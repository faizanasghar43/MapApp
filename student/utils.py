from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
import datetime

from .models import Student
from django.contrib.auth import get_user_model

User = get_user_model()

def login_employee(request, format=None):
    email = request.data.get("email")
    password = request.data.get("password")
    email = email.lower()
    print(email, password)
    data = login_employee_using_email_password(email, password)
    return Response(data, status=status.HTTP_200_OK)

def login_employee_using_email_password(email, password, throw_exception=True, is_password_encrypted=False):
    if email is None:
        raise ValidationError('Email should not be empty')
    if password is None:
        raise ValidationError('Password should not be empty')
    try:
        user = User.objects.get(email=email)
        student = Student.objects.get(user=user)
        user = authenticate(request=None, email=email, password=password)  # Use the custom authenticate function
        if user is not None:
            data = get_access_and_refresh_token_for_employee(user)
            return data
        else:
            if throw_exception:
                raise ValidationError('Invalid login credentials')
    except User.DoesNotExist or Student.DoesNotExist:
        raise ValidationError('Student does not exist')


    return False


def get_access_and_refresh_token_for_employee(employee):
    if employee is not None:

        if employee.last_login is None:

            refresh = RefreshToken.for_user(employee)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'last_login': employee.last_login
            }
            employee.last_login = datetime.datetime.now()
            employee.save()
            return data
        else:

            refresh = RefreshToken.for_user(employee)
            data = {
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token),
                'last_login': employee.last_login

            }
            employee.last_login = datetime.datetime.now()
            employee.save()
            return data