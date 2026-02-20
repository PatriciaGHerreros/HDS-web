from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Categoria, Recurso
from django.utils.html import format_html

# 1. POST (Con Summernote + Decorador)
@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('contenido',) # Activamos el editor rico para el contenido
    list_display = ('titulo', 'categoria', 'fecha_publicacion') # Columnas visibles
    list_filter = ('categoria', 'fecha_publicacion') # Filtros laterales
    search_fields = ('titulo', 'contenido') # Barra de búsqueda
    

# 2. CATEGORÍA (Decorador)
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre',) # Simple, solo el nombre


# 3. RECURSO (Decorador)
@admin.register(Recurso)
class RecursoAdmin(SummernoteModelAdmin):
    summernote_fields = ('descripcion',)
    
    # IMPORTANTE: Definimos que el click para entrar esté SOLO en el título
    list_display = ('mostrar_miniatura', 'titulo', 'categoria', 'orden')
    list_display_links = ('titulo',) # <--- Esto evita que hagas click en "Sin imagen"
    
    list_filter = ('categoria',)
    list_editable = ('orden',)

    def mostrar_miniatura(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" style="width: 50px; height: 35px; object-fit: cover; border-radius: 4px;" />', obj.imagen.url)
        
       # Si no hay imagen, devolvemos un texto vacío para que no rompa format_html
        return ""
    
    mostrar_miniatura.short_description = "Vista Previa"