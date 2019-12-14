from rest_framework import viewsets, permissions

from .models import Brewery
from .serializers import BrewerySerializer


class BreweryViewset(viewsets.ModelViewSet):
    queryset = Brewery.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = BrewerySerializer
