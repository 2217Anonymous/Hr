from rest_framework import serializers
from authentication import models as auth_model

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = auth_model.User
        fields = '__all__'