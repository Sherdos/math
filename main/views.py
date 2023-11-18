from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from main import serializers

# Create your views here.


def index(request):
    return render(request, 'index.html')

def calculator(request):
    return render(request, 'calculator.html')

def discriminant(request):
    return render(request, 'discriminant.html')



class TaskAPIView(APIView):
    def post(self, request, *args, **kwargs):
        
        serializer = serializers.TaskSerializer()
        return Response(serializer.data.keys(), status=status.HTTP_200_OK)