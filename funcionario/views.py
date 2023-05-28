from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import FuncionarioForm
from .models import Funcionario


# Create your views here.
def cadastro (request):
    form = FuncionarioForm()
    data = {'form': form}
    return render(request, 'funcionario/cadastro.html', data)

def cadastrados (request):
    funcionarios = Funcionario.objects.all()
    return render(request, 'funcionario/cadastrados.html', {'funcionarios':funcionarios })

def funcionario_novo(request):
    form = FuncionarioForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('funcionario/funcionario_cadastrado')

def funcionario_update(request, id):
    data ={}
    funcionario = Funcionario.objects.get(id=id)
    form = FuncionarioForm(request.POST or None, instance=funcionario)
    data['funcionario'] = funcionario
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('funcionario_cadastrado')
    else:
        return render(request, 'update.html', data)
    

def funcionario_delete(request, id):
    funcionario = Funcionario.objects.get(id=id)
    if request.method == 'POST':
        funcionario.delete()
        return redirect('funcionario_cadastrado')
    else:
        return render(request, 'delete_confirm.html', {'funcionario':funcionario})