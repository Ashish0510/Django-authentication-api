from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import UserRegistrationserializer,UserLoginSerializer,UserProfileSerializer,UserPaschangeSerializer, UserSendEmailSerializer, UserResetPassSerializer
from django.contrib.auth import authenticate
from authapp.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserRegistrationserializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
          user=serializer.save()
          token=get_tokens_for_user(user)
          return Response({'token':token,'msg':'registration successfull'},status=status.HTTP_201_CREATED)
        return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
      serializer=UserLoginSerializer(data=request.data)
      if serializer.is_valid(raise_exception=True):
          email=serializer.data.get("email")
          password=serializer.data.get("password")
          user= authenticate(email=email,password=password)
          if user is not None:
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':'login successfull'},status=status.HTTP_200_OK)
          else:
            return Response({'errors':{'non_field_errors':['email or password is not valid']}},status=status.HTTP_400_BAD_REQUEST) 
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serializer=UserProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK)

class UserPaschangeView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serializer=UserPaschangeSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password has been changed succesfully'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class SendEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serializer=UserSendEmailSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'for password reset link has been sent to ur email'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserResetPasswordView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,uid,token,format=None):
      serializer= UserResetPassSerializer(data=request.data,context={'uid':uid,'token':token})
      if serializer.is_valid(raise_exception=True):
       return Response({'msg':'password reset succesfully'},status=status.HTTP_200_OK)
      return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)






