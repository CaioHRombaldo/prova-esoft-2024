from .models import Curso, Disciplina
from django import forms

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

        label = {
        "title" : "Title",
        "description" : "Description",
        }

        widgets ={
        "title" : forms.TextInput(attrs={"placeholder":"Buy Groceries"}),
        "description" : forms.TextInput(attrs={"placeholder":"Visit super market and buy some groceries"}), 
        }

class DisciplinaForm(forms.ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'

        label = {
        "title" : "Title",
        "description" : "Description",
        }

        widgets ={
        "title" : forms.TextInput(attrs={"placeholder":"Buy Groceries"}),
        "description" : forms.TextInput(attrs={"placeholder":"Visit super market and buy some groceries"}), 
        }