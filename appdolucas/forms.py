from django import forms
from .models import Task

#Cria a classe TaskForm onde tem dois fields criados, um para o título e outro para a descrição 

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
