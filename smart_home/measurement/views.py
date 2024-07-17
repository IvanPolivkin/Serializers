# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer, MeasurementCreateSerializer

class SensorsView(ListCreateAPIView):
  queryset = Sensor.objects.all()
  serializer_class = SensorSerializer

class MeasurementsAddView(CreateAPIView):    #добавление измерения
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer

class SensorView(RetrieveUpdateAPIView):  #Изменение датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'

class SensorDeleteView(DestroyAPIView):  #Удаление датчика
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    lookup_field = 'id'

class SensorOneView(RetrieveAPIView):  # Показывает один датчик
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer
    lookup_field = 'id'