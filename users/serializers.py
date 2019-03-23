from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import Serializers
from .models import User


class UserSerializer(serializers.ModelSerializer)
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')

class CustomRegisterSerializer(RegisterSerializer):
    is_student = serializers.BooleanField()
    is_teacher = serializers.BooleanField()
    class Meta:
        model = User
        fields = ('email', 'username', 'password', 'is_student', 'is_teacher')