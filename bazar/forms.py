from django import forms
from bazar.models import *
from django.contrib.auth.forms import AuthenticationForm 

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'username'}))
    password = forms.CharField(label="Password", max_length=30, widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password'}))

class PessoaForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="Nome", widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'nome'}))
    email = forms.EmailField(max_length=128, help_text="Email", widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email'}))
    telefone = forms.CharField(max_length=16, help_text="Telefone", widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'telefone', 'data-mask': '(00) 0 0000-0000'}))

    class Meta:
        model = Pessoa
        fields = ('nome', 'email', 'telefone',)

class VendaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Pessoa
        exclude = ('category',)

class ProdutoForm(forms.ModelForm):
    tag = forms.CharField(max_length=128, help_text='Tag', widget=forms.TextInput(attrs={'class': 'form-control', 'name': 'Tag'}))
    preco = forms.DecimalField(help_text='Preco', widget=forms.NumberInput(attrs={'class': 'form-control', 'name': 'Preco'}))
    fornecedor = forms.ModelChoiceField(queryset=Pessoa.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'name': 'Fornecedor'}))

    class Meta:
        model = Produto
        fields = ('tag', 'preco', 'fornecedor', )
        # labels = {'fornecedor': 'Fornecedor'}


class CategoriaRoupaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Categoria_roupa
        exclude = ('category',)

class CategoriaCalcadoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Categoria_calcado
        exclude = ('category',)

class CategoriaAderecoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Categoria_adereco
        exclude = ('category',)


class RoupaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")
    # tamanho = models.CharField(max_length=2)
    # file will be uploaded to MEDIA_ROOT/roupas
    # foto = models.ImageField(upload_to='roupas', null=True)
    # descricao = models.CharField(max_length=128, null=True)
    # produto = models.OneToOneField(Produto)
    # categoria = models.ForeignKey(Categoria_roupa)

    class Meta:
        model = Roupa
        fields = ('tamanho', 'foto', 'descricao', 'produto',)


    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

class CalcadoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Calcado
        exclude = ('category',)

class AderecoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        model = Adereco
        exclude = ('category',)
