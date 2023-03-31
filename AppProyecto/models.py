from django.db import models
from django.contrib.auth.models import User

class Catalogo(models.Model):
    vendedor = models.ForeignKey(User, blank=True,null=True,on_delete=models.CASCADE)
    titulo = models.CharField(max_length=60)
    autor = models.CharField(max_length=60)
    genero = models.CharField(max_length=60)
    precio = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to = 'libros',blank=True,null=True)
    fecha= models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return f"Titulo: {self.titulo} - Autor: {self.autor} - Precio: {self.precio}"
    
    class Meta:
        ordering = ['-fecha']
    
class Comentarios(models.Model):
    comentario = models.ForeignKey(Catalogo, related_name='comentarios',on_delete=models.CASCADE, null=True)
    nombre = models.CharField(max_length=40, blank=True)
    mensaje = models.CharField(max_length=1000)
    fecha= models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fecha']
    


