# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-02 06:54
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
                ('foto', models.ImageField(null=True, upload_to='aderecos')),
                ('descricao', models.CharField(max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Calcado',
            fields=[
                ('idroupa', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.CharField(max_length=2)),
                ('foto', models.ImageField(null=True, upload_to='calcados')),
                ('descricao', models.CharField(max_length=128, null=True)),
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
                ('preco', models.DecimalField(decimal_places=2, default=0, max_digits=7)),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Roupa',
            fields=[
                ('idroupa', models.AutoField(primary_key=True, serialize=False)),
                ('tamanho', models.CharField(max_length=2)),
                ('foto', models.ImageField(null=True, upload_to='roupas')),
                ('descricao', models.CharField(max_length=128, null=True)),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto')),
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
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.AutoField(primary_key=True, serialize=False)),
                ('senha', models.CharField(max_length=16)),
                ('pessoa', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bazar.Pessoa')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('idvenda', models.AutoField(primary_key=True, serialize=False)),
                ('data', models.DateField(auto_now=True)),
                ('comprador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Pessoa')),
                ('produto', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto')),
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
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto'),
        ),
        migrations.AddField(
            model_name='calcado',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Tipo_calcado'),
        ),
        migrations.AddField(
            model_name='adereco',
            name='produto',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='bazar.Produto'),
        ),
        migrations.AddField(
            model_name='adereco',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bazar.Tipo_adereco'),
        ),
    ]
