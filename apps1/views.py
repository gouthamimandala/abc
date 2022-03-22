from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def apps1_hero(request):
    return HttpResponse('movie special')