from rest_framework import serializers

from historia_olimpica.models import NocRegions, AthleteEvents


class NocRegionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NocRegions
        fields = '__all__'


class AthleteEventsSerializer(serializers.ModelSerializer):
    noc = NocRegionsSerializer()
    class Meta:
        model = AthleteEvents
        fields = '__all__'

