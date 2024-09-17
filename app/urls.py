from django.urls import path
from app.views import CursoListView, CursoDetailView, CursoCreateView, CursoDeleteView, CursoUpdateView

urlpatterns = [
    # path('curso/create/', CursoCreateView.as_view(), name='create-view'),

    path('cursos/', CursoListView.as_view(), name='list-view'),
    path("curso/<int:pk>/", CursoDetailView.as_view(), name="curso-detail"),
    path("curso/add/", CursoCreateView.as_view(), name="curso-add"),
    path("curso/<int:pk>/", CursoUpdateView.as_view(), name="curso-update"),
    path("curso/<int:pk>/delete/", CursoDeleteView.as_view(), name="curso-delete"),
]
