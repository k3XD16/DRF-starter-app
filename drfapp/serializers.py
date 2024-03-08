from rest_framework import serializers
from drfapp.models import Mobile

class MobileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mobile
        fields = (
            'brand',
            'model',
            'price',
            'specs',
            'discount',
        )
