from django import forms

class ContactoForm(forms.Form):
    # Definimos los campos que esperamos y sus validaciones de seguridad
    nombre = forms.CharField(label="Nombre", max_length=100, required=True)
    email = forms.EmailField(label="Email", required=True)
    mensaje = forms.CharField(label="Mensaje", widget=forms.Textarea, required=True)