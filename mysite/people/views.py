# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .models import Person
from .forms import PersonForm

def index(request):
    return render(request, 'people/welcome.html', {'welcome_message': 'welcome to the people inventory'})

def add(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/list')
        else:
            return render(request, 'people/add.html', {'form': form})
    else:
        return render(request, 'people/add.html')

def list(request):
    people = Person.objects.all()
    print people
    return render(request, 'people/list.html', {'people':people})