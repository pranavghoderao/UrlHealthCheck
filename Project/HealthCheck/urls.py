from django.urls import path
from HealthCheck import views

urlpatterns = [
    path('show',views.show,name="show"),
]