from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reviews/', views.reviews, name='reviews'),
    path('woodlands/', views.woodlandsreviews, name='woodlandsreviews'),
    path('humble/', views.humblereviews, name='humblereviews'),
    path('houston/', views.houstonreviews, name='houstonreviews'),
    path('gmaps/', views.gmaps, name='gmaps'),
]