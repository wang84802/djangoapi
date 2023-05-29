from rest_framework import serializers
from historys.models import PowerStatisticsDay


class HistorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PowerStatisticsDay
        fields = '__all__'

