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

class Usuario(models.Model):
	idusuario = models.AutoField(primary_key=True)
	pessoa = models.OneToOneField(Pessoa)
	senha = models.CharField(max_length=16)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.pessoa.nome

	def __unicode__(self):
		return self.pessoa.nome

class Produto(models.Model):
	idproduto = models.AutoField(primary_key=True)
	tag = models.CharField(max_length=128, unique=True)
	preco = models.DecimalField(default=0, max_digits=7, decimal_places=2)
	fornecedor = models.ForeignKey(Pessoa)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.tag

	def __unicode__(self):
		return self.tag

class Venda(models.Model):
	idvenda = models.AutoField(primary_key=True)
	comprador = models.ForeignKey(Pessoa)
	produto = models.OneToOneField(Produto)
	data = models.DateField(auto_now=True)
	
	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.comprador.nome+" | "+self.produto.nome

	def __unicode__(self):
		return self.comprador.nome+" | "+self.produto.nome

class Categoria_roupa(models.Model):
	idcategoria_roupa = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Categoria_calcado(models.Model):
	idcategoria_calcado = models.AutoField(primary_key=True)
	nome = models.CharField(max_length=128, unique=True)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.nome

	def __unicode__(self):
		return self.nome

class Categoria_adereco(models.Model):
	idcategoria_adereco = models.AutoField(primary_key=True)
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
	categoria = models.ForeignKey(Categoria_roupa)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.categoria.nome+' | '+self.descricao

	def __unicode__(self):
		return self.categoria.nome+' | '+self.descricao

class Calcado(models.Model):
	idroupa = models.AutoField(primary_key=True)
	numero = models.CharField(max_length=2)
	# file will be uploaded to MEDIA_ROOT/calcados
	foto = models.ImageField(upload_to='calcados', null=True)
	descricao = models.CharField(max_length=128, null=True)
	produto = models.OneToOneField(Produto)
	categoria = models.ForeignKey(Categoria_calcado)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.categoria.nome+' | '+self.descricao

	def __unicode__(self):
		return self.categoria.nome+' | '+self.descricao

class Adereco(models.Model):
	idroupa = models.AutoField(primary_key=True)
	# file will be uploaded to MEDIA_ROOT/aderecos
	foto = models.ImageField(upload_to='aderecos', null=True)
	descricao = models.CharField(max_length=128, null=True)
	produto = models.OneToOneField(Produto)
	categoria = models.ForeignKey(Categoria_adereco)

	def __str__(self):  #For Python 2, use __str__ on Python 3
		return self.categoria.nome+' | '+self.descricao

	def __unicode__(self):
		return self.categoria.nome+' | '+self.descricao