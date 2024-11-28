# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth.models import User
from django.core.signing import Signer
from django.core.mail import send_mail

signer = Signer()

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Get the user data from the request
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({"error": "Username and password are required."}, status=status.HTTP_400_BAD_REQUEST)

        # Create and save the user
        user = User.objects.create_user(username=username, password=password)

        # Generate verification URL (for example)
        verification_url = signer.sign(user.username)

        # Send verification email (optional)
        send_mail(
            'Verify your email address',
            f'Please verify your email by clicking on this link: {verification_url}',
            'noreply@example.com',  # Sender email
            [user.email],  # Receiver email
            fail_silently=False,
        )

        return Response({
            "message": "Signup successful",
            "verification_url": verification_url
        }, status=status.HTTP_201_CREATED)
