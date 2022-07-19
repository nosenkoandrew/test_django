from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('calc/', views.calc(), name='calc'),
]
