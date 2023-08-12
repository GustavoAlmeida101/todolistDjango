from django.shortcuts import render,redirect
from .models import lista


def home(request):
    tarefa = lista.objects.all()
    return render(request,'index.html',{"tarefas":tarefa})

def salvar(request):
    n_tarefa = request.POST.get('tarefa')
    dia = request.POST.get('dia')
    lista.objects.create(tarefa=n_tarefa,dia =dia)
    tarefa = lista.objects.all()
    return render(request,'index.html',{"tarefas":tarefa})

def excluir(request,id):
    tarefa = lista.objects.get(id=id)
    tarefa.delete()
    return redirect(home)
    
