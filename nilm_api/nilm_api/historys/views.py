# Create your views here.
from historys.models import PowerStatisticsDay
from historys.serializers import HistorySerializer
from rest_framework import viewsets, status
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import action


class HistoryViewSet(viewsets.ModelViewSet):
    queryset = PowerStatisticsDay.objects.all()[:1000]                         
    serializer_class = HistorySerializer
    parser_classes = (JSONParser,)    
    # /api/history/data/
    @action(detail=False)
    def data(self, request, pk=None):
        #device = get_object_or_404(PowerStatisticsDay, pk=pk)
        device = request.query_params.get('device', None)
        datestart = request.query_params.get('datestart', None)
        dateend = request.query_params.get('dateend', None)                
        if device == "all":
            history = PowerStatisticsDay.objects.filter(date__range=[datestart,dateend])      
        else:    
            history = PowerStatisticsDay.objects.filter(device=device).filter(date__range=[datestart,dateend])                                 
        serializer = self.get_serializer(history, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
