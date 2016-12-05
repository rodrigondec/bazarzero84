from django import forms
from bazar.models import *

class PessoaForm(forms.ModelForm):
    nome = forms.CharField(max_length=128, help_text="Nome", widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=128, help_text="Email", widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=16, help_text="Telefone", widget=forms.TextInput(attrs={'class': 'form-control', 'data-mask': '(00) 0 0000-0000'}))

    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa
        fields = ('nome', 'email', 'telefone',)

class VendaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class ProdutoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class Tipo_roupaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class Tipo_calcadoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class Tipo_aderecoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class RoupaForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        # If url is not empty and doesn't start with 'http://', prepend 'http://'.
        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

        return cleaned_data

class CalcadoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

class AderecoForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Pessoa.")

    class Meta:
        # Provide an association between the ModelForm and a model
        model = Pessoa

        # What fields do we want to include in our form?
        # This way we don't need every field in the model present.
        # Some fields may allow NULL values, so we may not want to include them...
        # Here, we are hiding the foreign key.
        # we can either exclude the category field from the form,
        exclude = ('category',)
        #or specify the fields to include (i.e. not include the category field)
        #fields = ('title', 'url', 'views')

