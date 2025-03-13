from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.template.exceptions import TemplateDoesNotExist
from .models import Llibre
from .forms import LlibreForm

def index(response):
    try:
        tpl = get_template("index.html")
        return render(response,"index.html")
    except TemplateDoesNotExist:
        return HttpResponse("Backend OK. Posa en marxa el frontend seguint el README.")

def llista_llibres(request):
    # Recuperem tots els llibres de la base de dades
    llibres = Llibre.objects.all()
    
    # Passar la informació al template
    return render(request, 'llista_llibres.html', {'llibres': llibres})

def add_llibre(request):
    if request.method == 'POST':
        form = LlibreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('llista_llibres')  # Redirect to the list view after saving
    else:
        form = LlibreForm()

    return render(request, 'add_llibre.html', {'form': form})