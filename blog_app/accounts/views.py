from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework import status
from rest_framework.views import APIView

#take data from request,serialize it , is_valid --check for custom validation defined in serializers.py if it is not valid than
#return response with errors else save serialized data and return response created
#in except return response bad request
class RegisterView(APIView):
    
    def post(self, request):
        try:
            data = request.data
            serializer = RegisterSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors,
                    'message' : 'something went so wrong'
                }, status = status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({
                'data' : {},
                'message' : 'your account is created'
            },status = status.HTTP_201_CREATED)
        except Exception as e:
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status = status.HTTP_400_BAD_REQUEST)

#take data from request,serialize it,check if it is valid and if not valid return error response
#if it is valid call get_jwt_token--uses the authenticate method to verify these credentials against the database.
#This generates a new JWT refresh token and access token for the authenticated user,
#The function returns a success message "login success" along with a dictionary containing the JWT tokens:'refresh': The JWT refresh token.'access': The JWT access token., we will use this access token as Authorization
class LoginView(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = LoginSerializer(data = data)
            if not serializer.is_valid():
                return Response({
                    'data' : serializer.errors,
                    'message' : 'something went so wrong'
                }, status = status.HTTP_400_BAD_REQUEST)
            serializer.get_jwt_token(serializer.data)
            return Response(response,status = status.HTTP_200_OK)
        except Exception as e:
            return Response({
                'data' : {},
                'message' : 'something went wrong'
            },status = status.HTTP_400_BAD_REQUEST)

