#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazarzero84.settings')

import django
django.setup()

from bazar.models import Categoria_roupa, Categoria_calcado, Categoria_adereco


def populate():
    add_categoria_roupa("blusa")
    add_categoria_roupa("vestido")
    add_categoria_roupa("calça")
    # add_categoria_roupa("")

    add_categoria_calcado("bota")
    add_categoria_calcado("sandalia")
    add_categoria_calcado("tenis")
    # add_categoria_calcado("")

    add_categoria_adereco("bolsa")
    add_categoria_adereco("colar")
    add_categoria_adereco("anel")
    # add_categoria_adereco("")

    for o in Categoria_roupa.objects.all():
        print unicode(o)

    for o in Categoria_calcado.objects.all():
        print unicode(o)

    for o in Categoria_adereco.objects.all():
        print unicode(o)

def add_categoria_roupa(n):
    o = Categoria_roupa.objects.get_or_create(nome=n)[0]
    o.save()
    return o

def add_categoria_calcado(n):
    o = Categoria_calcado.objects.get_or_create(nome=n)[0]
    o.save()
    return o

def add_categoria_adereco(n):
    o = Categoria_adereco.objects.get_or_create(nome=n)[0]
    o.save()
    return o

# Start execution here!
if __name__ == '__main__':
    print "Starting Bazar population script..."
    populate()