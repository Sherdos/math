from django.urls import path
from main import views

urlpatterns = [
    path('', views.index),
    path('calculator/', views.calculator, name='calculator'),
    path('discriminant/', views.discriminant, name='discriminant'),
    path('discriminant/work/', views.TaskAPIView.as_view(), name='discriminant_work'),
]
