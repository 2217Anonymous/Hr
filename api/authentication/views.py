from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated

from api.authentication.serislizers import UserSerializers
from authentication import models as auth_model

class UsersView(ModelViewSet):
    queryset            = auth_model.User.objects.all()
    serializer_class    = UserSerializers