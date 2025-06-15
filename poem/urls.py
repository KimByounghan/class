from django.urls import path
from . import views

urlpatterns = [
    path('poem/<int:poem_id>/', views.poem_detail, name='poem_detail'),
    path('poem/<int:poem_id>/generate_appreciation/', views.generate_appreciation, name='generate_appreciation'),
]

