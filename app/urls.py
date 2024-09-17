from django.urls import path
from .views import createCursoView, showCursoView, updateCursoView, deleteCursoView

urlpatterns = [
    # path('curso/create/', CursoCreateView.as_view(), name='create-view'),

    path('', createCursoView, name='curso_view'),
    path('show/', showCursoView, name='show_view'),
    path('update/<int:f_id>', updateCursoView, name= 'update_view'),
    path('delete/<int:f_id>', deleteCursoView, name= 'delete_view'),
]
