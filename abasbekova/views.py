from django.shortcuts import render
from .models import addcard
# Create your views here.
def index(requests):
    return render(requests, 'index.html', context={ 'add': addcard.objects.all()})