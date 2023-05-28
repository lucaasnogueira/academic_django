from django.db import models

# Create your models here.


class Cargo(models.Model):
    cargo = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.cargo


class Escolaridade(models.Model):
    escolaridade = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.escolaridade

class Titulação(models.Model):
    titulação = models.CharField(max_length=2, blank=False, null=False)

    def __str__(self):
        return self.titulação

class RegimeTrabalho(models.Model):
    regime = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.regime
    
class DataAdmissao(models.Model):
    admissão = models.DateField(auto_now_add=True)

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE,)
    escolaridade = models.ForeignKey(Escolaridade,on_delete=models.CASCADE,)
    titulacao = models.ForeignKey(Titulação,on_delete=models.CASCADE,)
    regime = models.ForeignKey(RegimeTrabalho,on_delete=models.CASCADE,)
    admissao = models.ForeignKey(DataAdmissao,on_delete=models.CASCADE,)

    def __str__(self):
        return self.nome