from django.shortcuts import render, redirect
from .forms import CursoForm
from .models import Curso


def createCursoView(request):
    form = CursoForm
    if request.method == "POST":
        form = CursoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("show_view")
    template_name = "app/curso.html"
    context = {"form": form}
    return render(request, template_name, context)

def showCursoView(request):
    obj = Curso.objects.all()
    template_name = "app/show.html"
    context = {"obj": obj}
    return render(request, template_name, context)

def updateCursoView(request, f_id):
    obj = Curso.objects.get(id=f_id)
    form = CursoForm(instance=obj)
    if request.method == "POST":
        form = CursoForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show_view")
    template_name = "app/curso.html"
    context = {"form": form}
    return render(request, template_name, context)

def deleteCursoView(request, f_id):
    obj = Curso.objects.get(id = f_id)
    if request.method == "POST":
        obj.delete()
        return redirect("show_view")
    template_name = "app/confirmation.html"
    context = {"obj": obj}
    return render(request, template_name, context)
