from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token

User = get_user_model()

class RegisterView(APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        phone = request.data.get("phone")
        name = request.data.get("name")
        password = request.data.get("password")

        # Validation
        if not phone or not name or not password:
            return Response(
                {"error": "phone, name and password are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(phone=phone).exists():
            return Response(
                {"error": "User with this phone already exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Create user
        user = User.objects.create_user(
            phone=phone,
            name=name,
            password=password
        )

        token, _ = Token.objects.get_or_create(user=user)

        return Response(
            {
                "message": "User registered successfully",
                "token": token.key
            },
            status=status.HTTP_201_CREATED
        )
