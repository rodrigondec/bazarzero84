# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-05 00:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adereco',
            fields=[
                ('idroupa', models.AutoField(primary_key=True, serialize=False)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Calcado',
            fields=[
                ('idroupa', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=2)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('idpessoa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('telefone', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('idproduto', models.AutoField(primary_key=True, serialize=False)),
                ('tag', models.CharField(max_length=128, unique=True)),
                ('preco', models.IntegerField(default=0)),
                ('comprador', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comprador', to='bazar.Pessoa')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fornecedor', to='bazar.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('idroupa', models.AutoField(primary_key=True, serialize=False)),
                ('tamanho', models.CharField(max_length=2)),
                ('cor', models.CharField(max_length=20)),
                ('descricao', models.CharField(max_length=128)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto')),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_adereco',
            fields=[
                ('idtipo_adereco', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_calcado',
            fields=[
                ('idtipo_calcado', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_roupa',
            fields=[
                ('idtipo_roupa', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='roupa',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Tipo_roupa'),
        ),
        migrations.AddField(
            model_name='calcado',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto'),
        ),
        migrations.AddField(
            model_name='calcado',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Tipo_calcado'),
        ),
        migrations.AddField(
            model_name='adereco',
            name='produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto'),
        ),
        migrations.AddField(
            model_name='adereco',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Tipo_adereco'),
        ),
    ]
