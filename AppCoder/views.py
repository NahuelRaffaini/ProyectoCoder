from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.db.models import Q
from .models import Curso, Profesor, Estudiante, Entregable
from .forms import BusquedaForm, CursoFormulario

# Create your views here.

def curso(req, nombre, camada):

    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
    <p>Curso: {curso.nombre} - Camada: {curso.camada} creado con éxito!</p>
    """)

def listar_cursos(req):

    lista = Curso.objects.all()

    return render(req, "lista_cursos.html", {"lista_cursos": lista})

def inicio(req):

    return render(req, "inicio.html")

def cursos(req):

    return render(req, "cursos.html")

def profesores(req):

    return render(req, "profesores.html")

def estudiantes(req):

    return render(req, "estudiantes.html")

def entregables(req):

    return render(req, "entregables.html")

def cursoFormulario(req):

    print('method', req.method)
    print('POST', req.POST)

    if req.method == 'POST':

        miFormulario = CursoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            curso = Curso(nombre=data["curso"], camada=data["camada"])
            curso.save()

            return render(req, "inicio.html")
    else:

        miFormulario = CursoFormulario()
        return render(req, "cursoFormulario.html", {"miFormulario": miFormulario})

def busquedaCamada(req):

    return render(req, "busquedaCamada.html")

def buscar(req: HttpRequest):

    if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        return render(req, "resultadosBusqueda.html", {"cursos": cursos})
    else:
        return HttpResponse(f"Debe agregar una camada")
    
def lista_profesores(req):

    profesores = Profesor.objects.all()

    return render(req, "listaProfesores.html", {"profesores": profesores})

class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"
    context_object_name = "cursos"

class CursoDetail(DetailView):
    model = Curso
    template_name = "curso_detail.html"
    context_object_name = "curso"

class CursoCreate(CreateView):
    model = Curso
    template_name = "curso_create.html"
    fields = ['nombre', 'camada', 'fecha_creacion']
    success_url = '/app-coder/listaCursos'

class CursoUpdate(UpdateView):
    model = Curso
    template_name = "curso_update.html"
    fields = ('__all__')
    success_url = '/app-coder/listaCursos'

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_delete.html"
    success_url = '/app-coder/listaCursos'

class ProfesorList(ListView):
    model = Profesor
    template_name = "profe_list.html"
    context_object_name = "profesores"

class ProfesorDetail(DetailView):
    model = Profesor
    template_name = "profe_detail.html"
    context_object_name = "profesor"

class ProfesorCreate(CreateView):
    model = Profesor
    template_name = "profe_create.html"
    fields = ['nombre', 'apellido', 'email']
    success_url = '/app-coder/listaProfe'

class ProfesorUpdate(UpdateView):
    model = Profesor
    template_name = "profe_update.html"
    fields = ('__all__')
    success_url = '/app-coder/listaProfe'

class ProfesorDelete(DeleteView):
    model = Profesor
    template_name = "profe_delete.html"
    success_url = '/app-coder/listaProfe'

class EstudianteList(ListView):
    model = Estudiante
    template_name = "estu_list.html"
    context_object_name = "estudiantes"

class EstudianteDetail(DetailView):
    model = Estudiante
    template_name = "estu_detail.html"
    context_object_name = "estudiante"

class EstudianteCreate(CreateView):
    model = Estudiante
    template_name = "estu_create.html"
    fields = ['nombre', 'apellido', 'email']
    success_url = '/app-coder/listaEstu'

class EstudianteUpdate(UpdateView):
    model = Estudiante
    template_name = "estu_update.html"
    fields = ('__all__')
    success_url = '/app-coder/listaEstu'

class EstudianteDelete(DeleteView):
    model = Estudiante
    template_name = "Estu_delete.html"
    success_url = '/app-coder/listaEstu'

class EntregableList(ListView):
    model = Entregable
    template_name = "entre_list.html"
    context_object_name = "entregables"

class EntregableDetail(DetailView):
    model = Entregable
    template_name = "entre_detail.html"
    context_object_name = "entregable"

class EntregableCreate(CreateView):
    model = Entregable
    template_name = "entre_create.html"
    fields = ['nombre', 'fechaDeEntrega', 'entregado', 'estudiante', 'link']
    success_url = '/app-coder/listaEntre'

class EntregableUpdate(UpdateView):
    model = Entregable
    template_name = "entre_update.html"
    fields = ('__all__')
    success_url = '/app-coder/listaEntre'

class EntregableDelete(DeleteView):
    model = Entregable
    template_name = "entre_delete.html"
    success_url = '/app-coder/listaEntre'


def filtrar_estudiantes(request):
    query = request.GET.get('q')
    estudiantes = Estudiante.objects.filter(
        Q(nombre__icontains=query) | Q(apellido__icontains=query)
    ) if query else Estudiante.objects.all()

    return render(request, 'estu_list.html', {'estudiantes': estudiantes})

def filtrar_profesores(request):
    query = request.GET.get('q')
    profesores = Profesor.objects.filter(
        Q(nombre__icontains=query) | Q(apellido__icontains=query)
    ) if query else Profesor.objects.all()

    return render(request, 'profe_list.html', {'profesores': profesores})

def filtrar_cursos(request):
    query = request.GET.get('q')
    cursos = Curso.objects.filter(
        Q(nombre__icontains=query) | Q(camada__icontains=query)
    ) if query else Curso.objects.all()

    return render(request, 'curso_list.html', {'cursos': cursos})