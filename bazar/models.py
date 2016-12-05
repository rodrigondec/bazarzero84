from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
	idpessoa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	telefone = models.CharField(max_length=16)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

class Produto(models.Model):
	idproduto = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=128, unique=True)
	preco = models.IntegerField(default=0)
	fornecedor = models.ForeignKey(Pessoa, related_name='fornecedor')
	comprador = models.ForeignKey(Pessoa, null=True, related_name='comprador')

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tag

class Tipo_roupa(models.Model):
	idtipo_roupa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

class Tipo_calcado(models.Model):
	idtipo_calcado = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

class Tipo_adereco(models.Model):
	idtipo_adereco = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

class Roupa(models.Model):
	idroupa = models.AutoField(primary_key=True)
	tamanho = models.CharField(max_length=2)
	cor = models.CharField(max_length=20)
	descricao = models.CharField(max_length=128)
	produto = models.ForeignKey(Produto)
	tipo = models.ForeignKey(Tipo_roupa)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome

class Calcado(models.Model):
	idroupa = models.AutoField(primary_key=True)
	numero = models.CharField(max_length=2)
	cor = models.CharField(max_length=20)
	descricao = models.CharField(max_length=128)
	produto = models.ForeignKey(Produto)
	tipo = models.ForeignKey(Tipo_calcado)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome

class Adereco(models.Model):
	idroupa = models.AutoField(primary_key=True)
	cor = models.CharField(max_length=20)
	descricao = models.CharField(max_length=128)
	produto = models.ForeignKey(Produto)
	tipo = models.ForeignKey(Tipo_adereco)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome