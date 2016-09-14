from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo

# Create your views here.
def home(request):
    """
    Renderiza el home con un listado de fotos
    :param request: objeto HttpRequest con los datos de la peticion
    :return: objeto HttpResponse con los datos de la respuesta
    """
    photos = Photo.objects.all().order_by('-created')  # recupera todas las fotos de la BD
    context = {'photos_list': photos[:4]}
    return render(request, "photos/home.html", context)