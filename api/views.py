from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

class SignupView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        
        return Response({"message": "Signup successful!"}, status=status.HTTP_201_CREATED)
