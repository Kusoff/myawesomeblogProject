from django.shortcuts import render
from .models import Event

def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})
