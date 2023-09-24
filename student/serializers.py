from rest_framework import serializers
from .models import Student  # Import your custom Student model from the same app
from rest_framework.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class StudentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll_number','email','password']

    def create(self, validated_data):

        # Generate a username by combining name and roll_number
        username = f"{validated_data['name']}_{validated_data['roll_number']}"
        new_user = User.objects.create(username=username,email=validated_data['email'],is_student=True)
        new_user.set_password(validated_data['password'])
        new_user.save()
        student = Student(
            name=validated_data['name'],
            roll_number=validated_data['roll_number'],
            user = new_user
        )
        
        student.save()
        return student
