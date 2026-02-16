from django.contrib import admin
from .models import Post # Importamos tu modelo Post

admin.site.register(Post) # Le decimos a Django: "Muéstrame esto en el admin"
