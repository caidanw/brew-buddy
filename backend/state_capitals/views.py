from rest_framework import viewsets, permissions

from .models import StateCapital
from .serializers import StateCapitalSerializer


class StateCapitalViewset(viewsets.ModelViewSet):
    queryset = StateCapital.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = StateCapitalSerializer
