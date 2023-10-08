# serializers.py
from rest_framework import serializers
from .models import Ai

class AiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ai
        fields = '__all__'