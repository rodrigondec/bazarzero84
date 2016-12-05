from django.shortcuts import render
from django.http import HttpResponse
from bazar.models import *

def index(request):
	tipo_roupa_list = Tipo_roupa.objects.all()
	context_dict = {'tipo_roupas': tipo_roupa_list, 'boldmessage': "I am bold font from the context"}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
	return render(request, 'index.html', context_dict)