# urls.py

from django.urls import path
from .views import DroneList, DroneDetail, MedicationList, MedicationDetail

urlpatterns = [
    path('drones/', DroneList.as_view(), name='drone_list'),
    path('drones/<int:pk>/', DroneDetail.as_view(), name='drone_detail'),
    path('medications/', MedicationList.as_view(), name='medication_list'),
    path('medications/<int:pk>/', MedicationDetail.as_view(), name='medication_detail'),
]
