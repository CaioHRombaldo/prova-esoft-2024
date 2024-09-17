from django.contrib import admin

from app.models import Curso, Disciplina

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'cargaHoraria', 'dataInicio']

@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']
