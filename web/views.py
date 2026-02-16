from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.urls import reverse_lazy 
from django.contrib import messages
from .models import Post
from .forms import ContactoForm # Importamos el archivo que acabas de crear

class HomeView(TemplateView):
    template_name = "index.html"

class SobreMiView(TemplateView):
    template_name = "sobre-mi.html"

class ServiciosView(TemplateView):
    template_name = "servicios.html"


class ContactoView(FormView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('home') # Al enviar, te manda al Inicio

    def form_valid(self, form):
        # Esta función se ejecuta solo si los datos son válidos
        
        # Simulamos el envío imprimiendo en la terminal
        print("--------------------------------------------------")
        print(f"NUEVO MENSAJE DE: {form.cleaned_data['nombre']}")
        print(f"EMAIL: {form.cleaned_data['email']}")
        print(f"MENSAJE: {form.cleaned_data['mensaje']}")
        print("--------------------------------------------------")

        return super().form_valid(form)
# -------------------------------------

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"
    ordering = ["-fecha_publicacion"]

class RecursosView(TemplateView):
    template_name = "recursos.html"

class ContactoView(FormView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # AÑADIMOS EL MENSAJE AQUÍ
        messages.success(self.request, '¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.')
        
        # Logs en terminal (para ti)
        print("--------- NUEVO MENSAJE ---------")
        print(f"Nombre: {form.cleaned_data['nombre']}")
        print("---------------------------------")
        
        return super().form_valid(form)

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"