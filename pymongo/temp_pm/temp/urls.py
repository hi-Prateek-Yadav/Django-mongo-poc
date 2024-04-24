from django.urls import path
from . import views

urlpatterns = [
    path('insert/', views.insert_data, name='insert_data'),
    path('retrieve/', views.retrieve_data, name='retrieve_data'),
]
