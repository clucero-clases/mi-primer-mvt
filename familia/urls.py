from django.urls import path
from familia import views


urlpatterns = [
    path('', views.index, name="index"),
    path('agregar/', views.agregar, name="agregar"),
    path('borrar/<identificador>', views.borrar, name="borrar"),
    path('buscar/', views.buscar, name="buscar"),
    path('agregar/<identificador>/domicilio/', views.domicilio, name="domicilio"),
    path('agregar/<identificador>/laboral/', views.laboral, name="laboral")
]
