from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AlunoForm
from .models import Aluno


# Create your views here.
def cadastro (request):
    form = AlunoForm()
    data = {'form': form}
    return render(request, 'aluno/cadastro_aluno.html', data)

def cadastrados (request):
    alunos = Aluno.objects.all()
    return render(request, 'aluno/cadastrados.html', {'alunos':alunos })

def aluno_novo(request):
    form = AlunoForm(request.POST or None)
    if form.is_valid():
        form.save()
    return redirect('aluno_cadastrado')

def aluno_update(request, id):
    data ={}
    aluno = Aluno.objects.get(id=id)
    form = AlunoForm(request.POST or None, instance=aluno)
    data['aluno'] = aluno
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('aluno_cadastrado')
    else:
        return render(request, 'update_aluno.html', data)
    

def aluno_delete(request, id):
    aluno = Aluno.objects.get(id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('aluno_cadastrado')
    else:
        return render(request, 'delete_confirm.html', {'aluno':aluno})