# Create your views here.
from sensors.models import Sensor
from sensors.serializers import SensorSerializer
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()[:1000]                         
    serializer_class = SensorSerializer
    parser_classes = (JSONParser,)    
    # /api/sensor/data/
    @action(detail=False)
    def data(self, request, pk=None):
        #device = get_object_or_404(Sensor, pk=pk)
        device = request.query_params.get('device', None)
        datestart = request.query_params.get('datestart', None)
        dateend = request.query_params.get('dateend', None)        
        page = int(request.query_params.get('page', None))
        interval = 10
        sensor = Sensor.objects.filter(device=device).filter(datetime__range=[datestart,dateend])[page*10-10:page*10]                                        
        serializer = self.get_serializer(sensor, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # /api/sensor/device/
    @action(detail=False)
    def device(self, request, pk=None):                
        device = Sensor.objects.values_list('device', flat=True).distinct()        
        return Response(device, status=status.HTTP_200_OK)

            

