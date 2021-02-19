from django.shortcuts import get_object_or_404, render, redirect
from .models import Location , Comentary
from .forms import preReg, LocationForm, ComentaryForm
from django.http import HttpResponse


def index(request):
   return render(request, 'index.html', {'title': 'Про нас'})


def locations(request):
   locations = Location.objects.all().order_by()
   return render(request, 'loc.html', {'title': 'Наши локации', 'locations': locations})


def get_location(request, location_id):
   location = get_object_or_404(Location, location_id=location_id)
   return render(request, 'getloc.html', {'location': location})


def created_event(request):
   if request.method == 'POST':
      form = preReg(request.POST)
      if form.is_valid():
         form.save()
         return redirect('reg_event')
   else:
      form = preReg()
   return render(request, 'eventreg.html', {'title': 'Запрос на мероприятие', 'form': form})


def edit_loc(request, location_id):
   location = get_object_or_404(Location, location_id=location_id)
   if request.method == 'POST':
      form = LocationForm(request.POST, instance=location)
      if form.is_valid():
         form.save()
         return redirect('location')
   else:
      form = LocationForm(instance=location)
   return render(request, 'editloc.html', {'title': 'Запрос на мероприятие', 'form': form})


def show_coment(request):
   coments = Comentary.objects.all().order_by()
   return render(request, 'coment.html', {'title': 'Coment', 'coments': coments})




def create_comment(request):
   if request.method == 'POST':
      form = ComentaryForm(request.POST)
      if form.is_valid():
         form.save()
         return redirect('coment')
   else:
      form = ComentaryForm()
   return render(request, 'addcoment.html', {'title': 'Добавить коментарий', 'form': form})






# Create your views here.
