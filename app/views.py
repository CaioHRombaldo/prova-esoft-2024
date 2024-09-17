from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from app.models import Curso


class CursoListView(ListView):
    model = Curso

class CursoDetailView(DetailView):
    queryset = Curso.objects.all()

    def get_object(self):
        obj = super().get_object()
        # obj.last_accessed = timezone.now()
        obj.save()
        return obj

class CursoCreateView(CreateView):
    model = Curso
    fields = ["name"]


class CursoUpdateView(UpdateView):
    model = Curso
    fields = ["name"]


class CursoDeleteView(DeleteView):
    model = Curso
    success_url = reverse_lazy("curso-list")