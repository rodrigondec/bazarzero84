from django.shortcuts import render
from django.http import HttpResponse
from bazar.models import *
from bazar.forms import PessoaForm
from django.contrib.auth.decorators import login_required

def index(request):
    roupas = Roupa.objects.all()
    calcados = Calcado.objects.all()
    aderecos = Adereco.objects.all()

    context_dict = {'roupas': roupas, 'calcados': calcados, 'aderecos': aderecos}

    return render(request, 'index.html', context_dict)

@login_required(login_url='/interna/login/')
def interna(request):
    context_dict = {}
    return render(request, 'interna/index.html', context_dict)

def roupas(request):
    roupas = Roupa.objects.all()
    tipos = Tipo_roupa.objects.all()
    
    context_dict = {'roupas': roupas, 'tipos' : tipos}

    return render(request, 'roupas.html', context_dict)

def calcados(request):
    calcados = Calcado.objects.all()
    tipos = Tipo_calcado.objects.all()

    context_dict = {'calcados': calcados, 'tipos': tipos}

    return render(request, 'calcados.html', context_dict)

def aderecos(request):
    aderecos = Adereco.objects.all()
    tipos = Tipo_adereco.objects.all()

    context_dict = {'aderecos': aderecos, 'tipos': tipos}

    return render(request, 'aderecos.html', context_dict)

@login_required(login_url='/admin/login/')
def interna(request):
    context_dict = {}
    return render(request, 'interna/index.html', context_dict)

@login_required(login_url='/admin/login/')
def add_pessoa(request):
    # A HTTP POST? 
    if request.method == 'POST':
        form = PessoaForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = PessoaForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'interna/add_pessoa.html', {'form': form})

