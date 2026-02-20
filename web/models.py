from django.db import models
from django.utils import timezone

# 1. NUEVO MODELO: CATEGORÍA
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorías" # Para que en el admin no ponga "Categorias"

# 2. MODELO POST ACTUALIZADO
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=300, blank=True, null=True, help_text="Una frase corta que enganche al lector.")
    imagen = models.ImageField(upload_to='blog_img/', blank=True, null=True, verbose_name="Imagen Principal")
    contenido = models.TextField()
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    # Enlace a la categoría (opcional, por si ya tienes posts creados)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True, related_name="posts")

    def __str__(self):
        return self.titulo
    
 # --- MODELO PARA RECURSOS ---
class Recurso(models.Model):
    # Definimos las categorías exactas que me has pedido
    CATEGORIAS = [
        ('VERIFICACION', 'Verificación y Análisis (Externo)'),
        ('GUIAS', 'Guías oficiales y Kits (Externo)'),
        ('EXCLUSIVO', 'Recursos Exclusivos HDS'),
    ]

    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(help_text="Breve explicación de para qué sirve.")
    # Hacemos que el enlace sea opcional con null=True y blank=True
    enlace = models.URLField(max_length=500, null=True, blank=True) 
    # Añadimos el campo para PDFs
    archivo_pdf = models.FileField(upload_to='recursos/pdfs/', null=True, blank=True, help_text="Sube un manual o guía en PDF")
    categoria = models.CharField(max_length=20, choices=CATEGORIAS, default='VERIFICACION')
    
    # Opcional: Icono de Bootstrap para que quede visual (ej: bi-shield-check)
    icono = models.CharField(max_length=50, default="bi-link-45deg", help_text="Código del icono Bootstrap (ej: bi-shield)")
    # NUEVO: Imagen en miniatura
    imagen = models.ImageField(upload_to='recursos/thumbnails/', null=True, blank=True, help_text="Miniatura de la web o recurso")
    # Para ordenar los recursos si quieres
    orden = models.IntegerField(default=0, help_text="Número bajo sale antes")

    def __str__(self):
        return self.titulo
        
    class Meta:
        ordering = ['orden', 'titulo']   