from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from material.serializer import *
from django.contrib.auth import authenticate
from account.renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


# Create your views here.


class DivisionApiView(APIView):
    renderer_classes = [UserRenderer]
    def post(self, request, format=None):
      serializer = DivisionSerializer(data=request.data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      
      return Response(serializer.data)


class AllDivisions(APIView):
    renderer_classes = [UserRenderer]
    def get(self, request, format=None):
        divisions = Division.objects.all()
        serializer = DivisionSerializer(divisions, many=True)
        return Response({'items':serializer.data})
