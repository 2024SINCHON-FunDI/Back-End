from django.shortcuts import render
from .serializers import UserSerializer, UserLoginSerializer
from rest_framework import views, status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class SignupView(views.APIView):
    def post(self, request):       
        data = request.data.copy()
        
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': '회원가입 성공', 'data': serializer.data})
        return Response({'message': '회원가입 실패', 'error': serializer.errors})

class LoginView(views.APIView):
    serializer_class= UserLoginSerializer
    def post(self, request):
        serializer = UserLoginSerializer(data = request.data)

        if serializer.is_valid():
            return Response({'message':'로그인 성공', 'data':serializer.validated_data})
        return Response({'message':'로그인 실패', 'error':serializer.errors})