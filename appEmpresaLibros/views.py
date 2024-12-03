from django.shortcuts import render, get_object_or_404
from .models import Editorial, Autor, Libro
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .forms import LibroForm
from django.shortcuts import redirect

# Vista de la portada de "Book Store"
def portada_view(request):
    # Usamos prefetch_related para reducir consultas cuando obtenemos editoriales y sus libros
    editoriales = Editorial.objects.prefetch_related('libros')
    recientes_por_editorial = {}
    for editorial in editoriales:
        libro = editorial.libros.order_by('-año_lanzamiento').first()
        recientes_por_editorial[editorial.nombre] = libro
    return render(request, 'portada.html', {'recientes_por_editorial': recientes_por_editorial})

from django.db.models import Q

def libro_list_view(request):
    
    libros = Libro.objects.select_related('editorial').prefetch_related('autores')

    search_query = request.GET.get('search', '') 
    if search_query:
        # Busca en el nombre, isbn, autor y editorial
        libros = libros.filter(
            Q(nombre__icontains=search_query) |  # Filtra por nombre
            Q(isbn__icontains=search_query) |    # Filtra por ISBN
            Q(autores__nombre__icontains=search_query) |  # Filtra por autor
            Q(editorial__nombre__icontains=search_query)  # Filtra por editorial
        ).distinct()  # Usamos distinct() para evitar resultados duplicados

    return render(request, 'libro_list.html', {
        'libros': libros,
        'search_query': search_query,  
    })


# Vista de detalles de un libro
def libro_detail_view(request, libro_id):
    # Usamos select_related y prefetch_related para obtener datos relacionados eficientemente
    libro = get_object_or_404(
        Libro.objects.select_related('editorial').prefetch_related('autores'), 
        pk=libro_id
    )
    return render(request, 'libro_detail.html', {'libro': libro})

# Vista de la lista de editoriales
def editorial_list_view(request):
    # No necesita optimización, ya que no se cargan relaciones complejas
    editoriales = Editorial.objects.all()
    return render(request, 'editorial_list.html', {'editoriales': editoriales})

# Vista de detalles de una editorial
def editorial_detail_view(request, editorial_id):
    # Prefetch de los libros relacionados con la editorial
    editorial = get_object_or_404(
        Editorial.objects.prefetch_related('libros'), 
        pk=editorial_id
    )
    return render(request, 'editorial_detail.html', {'editorial': editorial})

# Vista de la lista de autores
def autor_list_view(request):
    # No necesita optimización, ya que no se cargan relaciones complejas
    autores = Autor.objects.all()
    return render(request, 'autor_list.html', {'autores': autores})

# Vista para crear un libro
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
    # Prefetch de los libros relacionados con el autor
    autor = get_object_or_404(
        Autor.objects.prefetch_related('libros'), 
        pk=autor_id
    )
    return render(request, 'autor_detail.html', {'autor': autor})
