from rest_framework import serializers
from main import models

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Task
        fields = '__all__'