from django.shortcuts import render
from django.http import HttpResponse
from bazar.models import *
from bazar.forms import PessoaForm

def index(request):
	tipo_roupa_list = Tipo_roupa.objects.all()
	context_dict = {'tipo_roupas': tipo_roupa_list, 'boldmessage': "I am bold font from the context"}

	return render(request, 'index.html', context_dict)

def roupas(request):
    roupas = Roupa.objects.all()
    context_dict = {'roupas': roupas}

    return render(request, 'roupas.html', context_dict)

def calcados(request):
	tipo_roupa_list = Tipo_roupa.objects.all()
	context_dict = {'tipo_roupas': tipo_roupa_list, 'boldmessage': "I am bold font from the context"}

	return render(request, 'calcados.html', context_dict)

def aderecos(request):
	tipo_roupa_list = Tipo_roupa.objects.all()
	context_dict = {'tipo_roupas': tipo_roupa_list, 'boldmessage': "I am bold font from the context"}

	return render(request, 'aderecos.html', context_dict)

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
    return render(request, 'add_pessoa.html', {'form': form})