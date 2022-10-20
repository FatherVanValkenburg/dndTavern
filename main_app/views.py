from django.shortcuts import render
from .models import hero

def home(request):
  return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def heroes_index(request):
  heroes = hero.objects.all()
  return render(request, 'heroes/index.html', { 'heroes': heroes})
def hero_detail(request,hero_id):
  heroes = hero.objects.get(id=hero_id)
  return render(request, 'heroes/detail.html', { 'hero': heroes})
