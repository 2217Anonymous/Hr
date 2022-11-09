from rest_framework import serializers
from helpers.models import TrackingModel

class TrackingModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = TrackingModel
        fields = '__all__'