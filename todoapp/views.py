from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import TodoItem
from .serializers import TodoItemSerializer
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.authentication import  BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

class TodoItemListView(generics.ListCreateAPIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer

class TodoItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer
class ATodoItemListView(viewsets.ModelViewSet):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TodoItem.objects.all()
    serializer_class = TodoItemSerializer



