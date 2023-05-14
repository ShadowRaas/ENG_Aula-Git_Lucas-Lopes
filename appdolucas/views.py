from django.shortcuts import render, redirect
from .models import Task

#Função que renderiza a home
def home(request):
  tasks = Task.objects.all()
  context = { "tasks": tasks }
  return render(request, "home.html", context=context)

#Função que faz o formulário que cria os interesses, tasks ou o que estiver sendo criado no seu projeto
def create_task(request):
 
  if request.method == "POST":
    Task.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
    )
    return redirect("home")
  
  return render(request, "task_form.html")

#Função que te leva de volta ao mesmo formulário que foi feito anteriormente referente ao objeto escolhido, seja task, interesses, entre outros
def update_task(request, task_id):
  task = Task.objects.get(id=task_id)
  
  if request.method == "POST":
      task.title = request.POST["title"]
      task.description=request.POST["description"]
      task.save()
      return redirect("home")

  return render(request, "task_form.html", context={"task": task})


#Função que faz o formulário para deletar o objeto escolhido, seja task, interesses, entre outros
def delete_task(request, task_id):
  task = Task.objects.get(id=task_id)
  if request.method == "POST":
    if "confirm" in request.POST:
      task.delete()

    return redirect("home")

  return render(request, "delete_form.html", context={"task": task})