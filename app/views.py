from django.shortcuts import render, redirect
from .forms import CursoForm, DisciplinaForm
from .models import Curso, Disciplina


def indexView(request):
    cursos = Curso.objects.all()
    disciplinas = Disciplina.objects.all()
    template_name = 'app/index.html'
    context = {"cursos": cursos, "disciplinas": disciplinas}
    return render(request, template_name, context)

def createCursoView(request):
    form = CursoForm
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("curso_show_view")
    template_name = "app/curso.html"
    context = {"form": form}
    return render(request, template_name, context)

def showCursoView(request):
    obj = Curso.objects.all()
    template_name = "app/curso_show.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def updateCursoView(request, f_id):
    obj = Curso.objects.get(id=f_id)
    form = CursoForm(instance=obj)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("curso_show_view")
    template_name = "app/curso.html"
    context = {"form": form}
    return render(request, template_name, context)

def deleteCursoView(request, f_id):
    obj = Curso.objects.get(id = f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("curso_show_view")
    template_name = "app/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def createDisciplinaView(request):
    form = DisciplinaForm
    if request.method == "POST":
        form = DisciplinaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("disciplina_show_view")
    template_name = "app/disciplina.html"
    context = {"form": form}
    return render(request, template_name, context)

def showDisciplinaView(request):
    obj = Disciplina.objects.all()
    template_name = "app/disciplina_show.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def updateDisciplinaView(request, f_id):
    obj = Disciplina.objects.get(id=f_id)
    form = DisciplinaForm(instance=obj)
    if request.method == "POST":
        form = DisciplinaForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("disciplina_show_view")
    template_name = "app/disciplina.html"
    context = {"form": form}
    return render(request, template_name, context)

def deleteDisciplinaView(request, f_id):
    obj = Disciplina.objects.get(id = f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("disciplina_show_view")
    template_name = "app/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)
