from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import request
from rest_framework import status
from .models import User
from django.utils.crypto import get_random_string
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class SignUp(APIView):
    def post(self, request):
        data = request.data
        user = User.objects.filter(mobile=data.get('mobile')).first()
        if user:
            return Response({
                'error': True,
                'message': 'This mobile number is already associated another account'
            }, status=status.HTTP_200_OK)
        username = get_random_string(length=32)
        user = User.objects.create(mobile=data.get('mobile'), username=username)
        user.first_name = data.get('name','')
        user.blood_group = data.get('blood_group','A+')
        user.gender = data.get('gender')
        user.dob = data.get('dob')
        user.set_password(data.get('password',''))
        user.save()
        token = Token.objects.create(user=user)
        return Response(data={
            'data': data,
            'token': token.key
        },status=status.HTTP_200_OK)

class GoogleToken(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        data = request.data
        user = request.user
        user.gcm = data.get('gcm','')
        user.save()
        return Response(data={
            'error': False,
            'message': 'Token saved successfully'
        },status=status.HTTP_200_OK)

class UserToken(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        user = request.user
        return Response(data={
            'user': user.id
        })