from django.urls import path, include
from .views import HospitalsList, HospitalDetail

urlpatterns = [
    path('hospital/', HospitalsList.as_view(), name="create hospital, list-all hospitals"),
    path('hospital/<int:pk>/', HospitalDetail.as_view(), name="details-one-hospital"),
]