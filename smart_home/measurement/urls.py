from django.urls import path
from measurement.views import SensorsView, MeasurementsAddView, SensorView, SensorDeleteView, SensorOneView

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensor/<id>/', SensorView.as_view()),
    path('add_measurements/', MeasurementsAddView.as_view()),
    path('sensor_delete/<id>/', SensorDeleteView.as_view()),
    path('sensorone/<id>/', SensorOneView.as_view()),
]
