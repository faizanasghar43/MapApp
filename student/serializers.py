from rest_framework import serializers
from .models import Student  # Import your custom Student model from the same app


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['email', 'name', 'roll_number', 'password']

    def create(self, validated_data):
        # Generate a username by combining name and roll_number
        username = f"{validated_data['name']}_{validated_data['roll_number']}"

        student = Student(
            email=validated_data['email'],
            name=validated_data['name'],
            roll_number=validated_data['roll_number'],
            username=username  # Set the generated username
        )
        student.set_password(validated_data['password'])
        student.save()
        return student
