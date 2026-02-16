from django.urls import path
from django.views.generic import TemplateView
from .views import HomeView, SobreMiView, ServiciosView, BlogListView, ContactoView, RecursosView, BlogDetailView

urlpatterns = [
    # Ruta vacía ('') significa la página principal
    path('', HomeView.as_view(), name='home'),
    
    # Rutas específicas
    path('sobre-mi/', SobreMiView.as_view(), name='sobre_mi'),
    path('servicios/', ServiciosView.as_view(), name='servicios'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
    path('contacto/', ContactoView.as_view(), name='contacto'),
    path('recursos/', RecursosView.as_view(), name='recursos'),
    path('legal/', TemplateView.as_view(template_name="legal.html"), name='legal'),
]