from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about),
  path('heroes/', views.heroes_index),
  path('heroes/<int:hero_id>/', views.hero_detail, name='detail'),
  path('heroes/create/', views.heroCreate.as_view(), name= 'hero_create'),
  path('heroes/<int:pk>/delete/', views.heroDelete.as_view(), name='hero_Delete'),
  path('heroes/<int:pk>/update/', views.HeroUpdate.as_view(), name='hero_Update'),
  path('accounts/signup/', views.signup, name='signup'),

]