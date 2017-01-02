from django.shortcuts import render
from django.http import HttpResponse
from bazar.models import *
from bazar.forms import *
from django.contrib.auth.decorators import login_required

def index(request):
    roupas = Roupa.objects.all()
    calcados = Calcado.objects.all()
    aderecos = Adereco.objects.all()

    context_dict = {'roupas': roupas, 'calcados': calcados, 'aderecos': aderecos}

    return render(request, 'index.html', context_dict)

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

@login_required(login_url='/admin/login/')
def add_produto(request):
    # A HTTP POST? 
    if request.method == 'POST':
        form = ProdutoForm(request.POST)

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
        form = ProdutoForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'interna/add_produto.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_categoria_roupa(request):
    if request.method == 'POST':
        form = CategoriaRoupaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoriaRoupaForm()

    return render(request, 'interna/add_categoria_roupa.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_roupa(request):
    if request.method == 'POST':
        form = RoupaForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = RoupaForm()

    return render(request, 'interna/add_roupa.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_categoria_calcado(request):
    if request.method == 'POST':
        form = CategoriaCalcadoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoriaCalcadoForm()

    return render(request, 'interna/add_categoria_calcado.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_calcado(request):
    if request.method == 'POST':
        form = CalcadoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CalcadoForm()

    return render(request, 'interna/add_calcado.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_categoria_adereco(request):
    if request.method == 'POST':
        form = CategoriaAderecoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = CategoriaAderecoForm()

    return render(request, 'interna/add_categoria_adereco.html', {'form': form})

@login_required(login_url='/admin/login/')
def add_adereco(request):
    if request.method == 'POST':
        form = AderecoForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print form.errors
    else:
        form = AderecoForm()

    return render(request, 'interna/add_adereco.html', {'form': form})
