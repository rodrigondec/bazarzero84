from __future__ import unicode_literals

from django.db import models

class Pessoa(models.Model):
	idpessoa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128)
	email = models.CharField(max_length=128)
	telefone = models.CharField(max_length=16)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Venda(models.Model):
	idvenda = models.AutoField(primary_key=True)
	comprador = models.ForeignKey(Pessoa)
	data = models.DateField(auto_now=True)
	
	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.comprador.nome

	def __unicode__(self):
		return self.comprador.nome

class Produto(models.Model):
	idproduto = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=128, unique=True)
	preco = models.IntegerField(default=0)
	fornecedor = models.ForeignKey(Pessoa)
	venda = models.ForeignKey(Venda, null=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tag

	def __unicode__(self):
		return self.tag

class Tipo_roupa(models.Model):
	idtipo_roupa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Tipo_calcado(models.Model):
	idtipo_calcado = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Tipo_adereco(models.Model):
	idtipo_adereco = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Roupa(models.Model):
	idroupa = models.AutoField(primary_key=True)
	tamanho = models.CharField(max_length=2)
	# file will be uploaded to MEDIA_ROOT/roupas
	foto = models.ImageField(upload_to='roupas', null=True)
	descricao = models.CharField(max_length=128, null=True)
	produto = models.OneToOneField(Produto)
	tipo = models.ForeignKey(Tipo_roupa)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome+' | '+self.descricao

	def __unicode__(self):
		return self.tipo.nome+' | '+self.descricao

class Calcado(models.Model):
	idroupa = models.AutoField(primary_key=True)
	numero = models.CharField(max_length=2)
	# file will be uploaded to MEDIA_ROOT/calcados
	foto = models.ImageField(upload_to='calcados', null=True)
	descricao = models.CharField(max_length=128, null=True)
	produto = models.OneToOneField(Produto)
	tipo = models.ForeignKey(Tipo_calcado)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome+' | '+self.descricao

	def __unicode__(self):
		return self.tipo.nome+' | '+self.descricao

class Adereco(models.Model):
	idroupa = models.AutoField(primary_key=True)
	# file will be uploaded to MEDIA_ROOT/aderecos
	foto = models.ImageField(upload_to='aderecos', null=True)
	descricao = models.CharField(max_length=128, null=True)
	produto = models.OneToOneField(Produto)
	tipo = models.ForeignKey(Tipo_adereco)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tipo.nome+' | '+self.descricao

	def __unicode__(self):
		return self.tipo.nome+' | '+self.descricao