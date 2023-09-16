from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import StudentSerializer
from rest_framework.response import Response
from .models import Student  # Import your custom Student model
from .utils import login_employee


class RegisterUser(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'errors': serializer.errors, 'message': 'Something went wrong'})

        # Save the student (custom User) object
        student = serializer.save()

        # Generate a token for the newly created student
        token, created = Token.objects.get_or_create(user=student)

        return Response({
            'status': 200, 'payload': serializer.data, 'token': str(token), 'message': 'Your data has been saved'
        })


class LoginUser(ObtainAuthToken):
    def post(self, request, format=None):
        return login_employee(request)


