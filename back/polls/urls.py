from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
	path('nueva/', views.nueva),
	path('getHojas/', views.getHojas),	
    path('getHoja/', views.getHoja), 
    path('actualizar/', views.actualizar),   
    path('borrar/', views.borrar),    
]