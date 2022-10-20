from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import hero

class heroCreate(CreateView):
  model = hero
  fields = ['name', 'job', 'description', 'race', 'age']
  success_url = '/heroes/'

class HeroUpdate(UpdateView):
    model = hero
    fields = ['name', 'job', 'description', 'race', 'age']
    success_url = '/heroes/'
class heroDelete(DeleteView):
  model = hero
  success_url = '/heroes/'

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
