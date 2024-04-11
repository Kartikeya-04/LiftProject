from django.urls import path
from . import views
urlpatterns = [
    path('', views.Home),
    path('/Compute',views.Compute)
    
]