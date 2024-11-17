from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada_view, name='portada'),
    path('libros/', views.libro_list_view, name='libro_list'),
    path('libro/<int:libro_id>/', views.libro_detail_view, name='libro_detail'),
    path('editoriales/', views.editorial_list_view, name='editorial_list'),
    path('editorial/<int:editorial_id>/', views.editorial_detail_view, name='editorial_detail'),
    path('autores/', views.autor_list_view, name='autor_list'),
    path('autor/<int:autor_id>/', views.autor_detail_view, name='autor_detail'),
]
