from rest_framework import serializers
from sensors.models import Sensor


class SensorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sensor
        fields = '__all__'
        #fields = ('id', 'datetime', 'device', 'vo', 'cu', 'active','reactive','apparent','pf','freq')

