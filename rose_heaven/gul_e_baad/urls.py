from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.home, name='gul_e_baad/home'),
    
]
