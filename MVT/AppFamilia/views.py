from django.shortcuts import render
from django.template import loader
from django.template import Template, Context
from django.http import HttpResponse
from AppFamilia.models import Familiar
# Create your views here.

def mis_familiares(request):
    template = loader.get_template('familia.html')
    documento = template.render({
        'familiares': Familiar.objects.all()
    })
    return HttpResponse(documento)
    