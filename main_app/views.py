from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import hero

def signup(request):
  error_message = ''
  if request.method == 'POST':

    form = UserCreationForm(request.POST)
    if form.is_valid():

      user = form.save()

      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class heroCreate(CreateView):
  model = hero
  fields = ['name', 'job', 'description', 'race', 'age']
def form_valid(self, form):
  form.instance.user = self.request.user
  return super().form_valid(form)
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
@login_required
def heroes_index(request):
    heroes = hero.objects.filter(user=request.user)
    return render(request, 'heroes/index.html', { 'heroes': heroes })
@login_required
def hero_detail(request,hero_id):
  heroes = hero.objects.get(id=hero_id)
  return render(request, 'heroes/detail.html', { 'hero': heroes})
