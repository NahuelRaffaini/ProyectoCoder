from django.contrib import admin
from .models import Curso, Profesor, Estudiante, Entregable
from datetime import datetime

class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'camada', 'fecha_creacion', 'antiguedad']
    search_fields = ['nombre', 'camada']
    list_filter = ['nombre']

    def antiguedad(self, object):
        print('**********',object)
        if object.fecha_creacion:
            return (datetime.now().date() - object.fecha_creacion).days

# Register your models here.
admin.site.register(Curso, CursoAdmin)
admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)