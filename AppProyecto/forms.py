from django import forms
from AppProyecto.models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CatalogoFormulario(forms.Form):
    titulo = forms.CharField()
    autor = forms.CharField()
    genero = forms.CharField()
    precio = forms.CharField()
    descripcion = forms.CharField()
    imagen = forms.ImageField(required=True)
    
    class Meta:
        model = User
        fields = ['vendedor', 'titulo', 'autor', 'genero', 'precio', 'descripcion', 'imagen']
        #Saca los mensajes
        help_text = {k:"" for k in fields}

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        #Saca los mensajes
        help_text = {k:"" for k in fields}

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label='Ingrese su email:')
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'last_name', 'first_name']
        #Saca los mensajes
        help_text = {k:"" for k in fields}



class NuevoComentario(forms.ModelForm):
    class Meta:
        model = Comentarios
        fields = ['nombre', 'mensaje']
        widgets = {'nombre' : forms.TextInput(attrs={'class': 'form-control'}),
                   'mensaje' : forms.Textarea(attrs={'class': 'form-control'})}


