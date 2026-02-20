from django.views.generic import TemplateView, ListView, FormView, DetailView
from django.urls import reverse_lazy 
from django.contrib import messages
from .models import Post, Recurso
from .forms import ContactoForm

# --- VISTAS ESTÁTICAS ---

class HomeView(TemplateView):
    template_name = "index.html"

class SobreMiView(TemplateView):
    template_name = "sobre-mi.html"

class ServiciosView(TemplateView):
    template_name = "servicios.html"

# --- VISTA DE CONTACTO (CBV con lógica de mensajes) ---

class ContactoView(FormView):
    template_name = "contacto.html"
    form_class = ContactoForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Lógica segura: añadimos el mensaje de éxito para el usuario
        messages.success(self.request, '¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.')
        
        # Logs en terminal para desarrollo (evitar datos sensibles en logs de producción reales)
        print("--------- NUEVO MENSAJE ---------")
        print(f"Nombre: {form.cleaned_data['nombre']}")
        print(f"Email: {form.cleaned_data['email']}")
        print("---------------------------------")
        
        return super().form_valid(form)

# --- VISTAS DE CONTENIDO DINÁMICO (BLOG) ---

class BlogListView(ListView):
    model = Post
    template_name = "blog.html"
    context_object_name = "posts"
    ordering = ["-fecha_publicacion"]

class BlogDetailView(DetailView):
    model = Post
    template_name = "post_detail.html"
    context_object_name = "post"

# --- VISTA DE RECURSOS (CBV con filtrado seguro) ---

class RecursosView(TemplateView):
    template_name = "recursos.html"

    def get_context_data(self, **kwargs):
        # Obtenemos el contexto base de la clase padre
        context = super().get_context_data(**kwargs)
        
        # Inyectamos los filtros de seguridad del ORM
        context['exclusivos'] = Recurso.objects.filter(categoria='EXCLUSIVO')
        context['verificacion'] = Recurso.objects.filter(categoria='VERIFICACION')
        context['guias'] = Recurso.objects.filter(categoria='GUIAS')
        
        return context