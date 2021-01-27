from rest_framework import viewsets

from historia_olimpica.models import AthleteEvents, NocRegions
from historia_olimpica.serializers import AthleteEventsSerializer, NocRegionsSerializer


class NocRegionsViewSet(viewsets.ModelViewSet):
    serializer_class = NocRegionsSerializer
    queryset = NocRegions.objects.all()


class AthleteEventsViewSet(viewsets.ModelViewSet):
    serializer_class = AthleteEventsSerializer
    queryset = AthleteEvents.objects.all()
