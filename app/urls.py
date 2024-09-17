from django.urls import path
from .views import indexView, createCursoView, showCursoView, updateCursoView, deleteCursoView, createDisciplinaView, showDisciplinaView, updateDisciplinaView, deleteDisciplinaView

urlpatterns = [
    path('', indexView, name='index_view'),

    path('cursos/', createCursoView, name='curso_view'),
    path('curso/show/', showCursoView, name='curso_show_view'),
    path('curso/update/<int:f_id>', updateCursoView, name= 'curso_update_view'),
    path('curso/delete/<int:f_id>', deleteCursoView, name= 'curso_delete_view'),

    path('disciplinas/', createDisciplinaView, name='disciplina_view'),
    path('disciplina/show/', showDisciplinaView, name='disciplina_show_view'),
    path('disciplina/update/<int:f_id>', updateDisciplinaView, name= 'disciplina_update_view'),
    path('disciplina/delete/<int:f_id>', deleteDisciplinaView, name= 'disciplina_delete_view'),
]
