from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view, permission_classes
from models.serializers import *
from authentication.emails.emails import new_account_email
from models.models import *

@api_view(["POST"])
def register_api(request):
    email = request.data.get("email")
    full_name = request.data.get("full_name")
    password = request.data.get("password")

    if not email or not full_name or not password:
        return Response({"error": "Email, password, and full name must not be empty"}, status=status.HTTP_400_BAD_REQUEST)

    if full_name:
        parts = full_name.split()
        first_name = parts[0]
        last_name = parts[1] if len(parts) > 1 else ''

    try:
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
        print(user)

        if user is not None:
            try:
                AccountEmail.objects.create(
                    email = user.email,
                )
                print("account email created")
                new_account_email(user.email, user.first_name)
            except Exception as e:
                    return Response({"error":f"Error sending email: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        else:
            return Response({"error":"Failed to send confirmation email"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        user_info = UserSerializer(user).data
        return Response(user_info, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": f"There was an error: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)