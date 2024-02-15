from django.urls import path
from . import views

urlpatterns = [
    path('introducir-socio/', views.introducir_socio),
    path('obtener-todos-socios/', views.obtener_todos_socios),
]
