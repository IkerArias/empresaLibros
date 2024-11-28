# forms.py
from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = ['nombre', 'isbn', 'año_lanzamiento', 'foto', 'editorial', 'autores']

    
    def clean_isbn(self):
        isbn = self.cleaned_data.get('isbn')
        # Validación del ISBN 
        if not isbn.isdigit():
            raise forms.ValidationError("El ISBN debe ser numérico")
        return isbn
