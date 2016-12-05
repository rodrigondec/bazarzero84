#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bazarzero84.settings')

import django
django.setup()

from bazar.models import Tipo_roupa, Tipo_calcado, Tipo_adereco


def populate():
    add_tipo_roupa("blusa")
    add_tipo_roupa("vestido")
    add_tipo_roupa("calça")
    # add_tipo_roupa("")

    add_tipo_calcado("bota")
    add_tipo_calcado("sandalia")
    add_tipo_calcado("tenis")
    # add_tipo_calcado("")

    add_tipo_adereco("bolsa")
    add_tipo_adereco("colar")
    add_tipo_adereco("anel")
    # add_tipo_adereco("")

def add_tipo_roupa(n):
    o = Tipo_roupa.objects.get_or_create(nome=n)[0]
    o.save()
    return o

def add_tipo_calcado(n):
    o = Tipo_calcado.objects.get_or_create(nome=n)[0]
    o.save()
    return o

def add_tipo_adereco(n):
    o = Tipo_adereco.objects.get_or_create(nome=n)[0]
    o.save()
    return o

# Start execution here!
if __name__ == '__main__':
    print "Starting Bazar population script..."
    populate()