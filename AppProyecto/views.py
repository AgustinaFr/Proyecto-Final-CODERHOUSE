from django.shortcuts import render
from django.http import HttpResponse
from AppProyecto.models import *
from AppProyecto.forms import *
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.hashers import make_password



# Create your views here.

def inicio(request):
  return render(request, 'AppProyecto/inicio.html')

def catalogo(request):
  return render(request, 'AppProyecto/catalogo.html')

@login_required
def MisLibros(request):
  vendedor = request.user.username
  ventas = Catalogo.objects.filter(vendedor= request.user)
  return render(request, 'AppProyecto/mislibros.html', {'ventas':ventas, 'vendedor':vendedor})

@login_required
def VenderLibro(request):
  if request.method == "POST":
    miFormulario = CatalogoFormulario(request.POST, request.FILES)
    print(miFormulario)
    if miFormulario.is_valid:
      informacion = miFormulario.cleaned_data
      venta = Catalogo(vendedor=request.user, titulo=informacion["titulo"], autor=informacion["autor"], genero = informacion["genero"], precio = informacion["precio"], descripcion = informacion["descripcion"], imagen = informacion['imagen'])
      venta.save()
      return render (request, "AppProyecto/catalogo.html")
  else:
    miFormulario = CatalogoFormulario()

  return render(request, 'AppProyecto/venderlibro.html',{"miFormulario":miFormulario})

def acercaDeMi(request):
  return render(request, 'AppProyecto/acercademi.html')

class CatalogoList(ListView):
  model = Catalogo
  template_name = "AppProyecto/catalogo_list.html"
 # template_name = "AppProyecto/catalogo.html"

class CatalogoDetalle(DetailView, LoginRequiredMixin):
  model = Catalogo
  template_name = "AppProyecto/catalogo_detalle.html"

class CatalogoUppdate(UpdateView, LoginRequiredMixin):
  model = Catalogo
  success_url = "/AppProyecto/catalogo/list"
 # success_url = "/AppProyecto/catalogo"
  fields = ['titulo', 'autor', 'genero', 'precio', 'descripcion', 'imagen']

class CatalogoDelete(DeleteView, LoginRequiredMixin):
  model = Catalogo
  success_url = "/AppProyecto/catalogo/list"
  #success_url = "/AppProyecto/catalogo"

def login_request(request):
  if request.method == 'POST':
    form = AuthenticationForm(request, data = request.POST)
    if form.is_valid():
      usuario = form.cleaned_data.get('username')
      contra = form.cleaned_data.get('password')
      user = authenticate(username=usuario, password=contra)

      if user is not None:
        login(request,user)
        return render(request,'AppProyecto/inicio.html', {'mensaje': f'Bienvenido {usuario}'})
      else:
        return render(request, 'AppProyecto/inicio.html',{'mensaje':"Error, datos incorrectos"})
    
    else:
      return render(request, 'AppProyecto/inicio.html',{'mensaje':"Error, formulario erroneo"})
  
  form = AuthenticationForm()
  return render (request, 'AppProyecto/login.html',{'form':form})

def register(request):
  if request.method == 'POST':
    form = UserRegisterForm(request.POST)
    
    if form.is_valid():
      username = form.cleaned_data['username']
      form.save()
      return render(request,'AppProyecto/inicio.html', {'mensaje':'Usuario creado'})
  
  else:
    form = UserRegisterForm()

  return render(request, 'AppProyecto/registro.html',{'form':form})

@login_required
def editarPerfil(request):
  usuario = request.user
  if request.method == 'POST':
    miFormulario = UserEditForm(request.POST)
    print(miFormulario)
    if miFormulario.is_valid():
      informacion = miFormulario.cleaned_data
      print(miFormulario)
      usuario.email = informacion['email']
      usuario.first_name = informacion['first_name']
      usuario.last_name = informacion['last_name']
      if informacion['password1'] == informacion['password2']:
        usuario.password = make_password(informacion['password1'])
        usuario.save()
      else:
        return render (request, 'AppProyecto/inicio.html', {'mensaje':'Contrasena incorrecta'})
      return render(request, 'AppProyecto/inicio.html')
  else:
    miFormulario = UserEditForm(initial={'email':usuario.email})
  return render (request, 'AppProyecto/editarPerfil.html', {'miFormulario':miFormulario, 'usuario':usuario})

class AgregarComentario(LoginRequiredMixin, CreateView):
  model = Comentarios
  form_class= NuevoComentario
  template_name='AppProyecto/comentario_form.html'
  success_url= reverse_lazy('List')
  
  def form_valid(self, form) :
    form.instance.comentario_id = self.kwargs['pk']
    return super(AgregarComentario, self).form_valid(form)
  



  