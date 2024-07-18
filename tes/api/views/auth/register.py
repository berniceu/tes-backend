from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from models.serializers import UserSerializer

@api_view(["POST"])
def register_api(request):
    email = request.data.get("email")
    full_name = request.data.get("full_name")
    password = request.data.get("password")

    if not email or not full_name or not password:
        return Response({"error": "Email, password, and full name must not be empty"}, status=status.HTTP_400_BAD_REQUEST)

    try:
        parts = full_name.split()
        first_name = parts[0] if len(parts) > 0 else ''
        last_name = parts[1] if len(parts) > 1 else ''

        validate_email(email)
        if User.objects.filter(email=email).exists():
            return Response({"error": "User with the same email already exists"}, status=status.HTTP_409_CONFLICT)

        user = User.objects.create(
            email=email,
            username=email,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password)
        )

        user_info = UserSerializer(user).data
        return Response(user_info, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": f"There was an error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)