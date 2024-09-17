from .models import Curso
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