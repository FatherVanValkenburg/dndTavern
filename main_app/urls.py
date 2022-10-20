from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about),
  path('heroes/', views.heroes_index),
  path('heroes/<int:hero_id>/', views.hero_detail, name='detail'),

]