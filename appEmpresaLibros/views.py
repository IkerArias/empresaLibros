from django.shortcuts import render, get_object_or_404
from .models import Editorial, Autor, Libro
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render, redirect
from .forms import LibroForm

# Vista de la portada de "Book Store"
def portada_view(request):
    # Obtener un libro de cada editorial (por ejemplo, el más reciente)
    recientes_por_editorial = {}
    editoriales = Editorial.objects.all()
    for editorial in editoriales:
        libro = editorial.libros.order_by('-año_lanzamiento').first()
        recientes_por_editorial[editorial.nombre] = libro
    return render(request, 'portada.html', {'recientes_por_editorial': recientes_por_editorial})

# Vista de la lista de libros
def libro_list_view(request):
    
    libros = Libro.objects.all()

    
    search_query = request.GET.get('search', '')  

   
    if search_query:
        libros = libros.filter(nombre__icontains=search_query)  

    
    return render(request, 'libro_list.html', {
        'libros': libros,
        'search_query': search_query,  
    })

# Vista de detalles de un libro
def libro_detail_view(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'libro_detail.html', {'libro': libro})

# Vista de la lista de editoriales
def editorial_list_view(request):
    editoriales = Editorial.objects.all()
    return render(request, 'editorial_list.html', {'editoriales': editoriales})

# Vista de detalles de una editorial
def editorial_detail_view(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    return render(request, 'editorial_detail.html', {'editorial': editorial})

# Vista de la lista de autores
def autor_list_view(request):
    autores = Autor.objects.all()
    return render(request, 'autor_list.html', {'autores': autores})

#Vista
class LibroCreateView(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libro_form.html'
    success_url = reverse_lazy('libro_list')
def crear_libro_view(request):
    if request.method == 'POST':
        form = LibroForm(request.POST, request.FILES)  # Para manejar archivos como imágenes
        if form.is_valid():
            form.save()  # Guarda el libro
            return redirect('libro_list')  # Redirige a la lista de libros después de guardar
    else:
        form = LibroForm()

    return render(request, 'crear_libro.html', {'form': form})

# Vista de detalles de un autor
def autor_detail_view(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'autor_detail.html', {'autor': autor})
