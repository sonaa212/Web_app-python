from django.shortcuts import render

from django.views.generic.list import ListView 
from .models import Tache

# Create your views here.

class ListeTache(ListView):
    model=Tache



