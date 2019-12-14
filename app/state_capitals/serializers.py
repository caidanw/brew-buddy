from rest_framework import serializers

from .models import StateCapital


class StateCapitalSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateCapital
        fields = '__all__'
