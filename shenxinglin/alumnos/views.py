from django.shortcuts import render

# Create your views here.
def inicio(request):
    return render(request, './alumnos/index.html')

def escuela(request):
    return render(request, './alumnos/escuela.html')

def noticias(request):
    return render(request, './alumnos/noticias.html')


def staff(request):
    return render(request, './alumnos/staff.html')

def alumnos(request):
    return render(request, './alumnos/alumnos.html')