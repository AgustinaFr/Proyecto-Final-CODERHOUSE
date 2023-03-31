from django.urls import path
from AppProyecto import views

urlpatterns = [
    path('', views.inicio, name= "Inicio"),
    path ('catalogo', views.catalogo, name="Catalogo"),
    path ('mislibros', views.MisLibros, name="MisLibros"),
    path ('venderlibro', views.VenderLibro, name="VenderLibro"),
    path ('acercademi', views.acercaDeMi, name="AcercaDeMi"),
    path('catalogo/list', views.CatalogoList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', views.CatalogoDetalle.as_view(), name='Detail'),
    path('detalle/<int:pk>', views.CatalogoUppdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.CatalogoDelete.as_view(), name='Delete'),
    path('login', views.login_request, name='Login'),
    path('register', views.register, name='Register'),
    path('logout', views.LogoutView.as_view(template_name='AppProyecto/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name='EditarPerfil'),
    path('detalle/<int:pk>/comentario/', views.AgregarComentario.as_view(), name = 'Comentario'),
   
    
]