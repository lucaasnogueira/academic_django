from django.db import models



class Turno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome
    
class Unidade(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.nome


class Serie(models.Model):
    serie = models.CharField(max_length=1, blank=False, null=False)

    def __str__(self):
        return self.serie

class Nivel(models.Model):
    nivel = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nivel


class Aluno(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=False)
    nome_responsavel = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    email_responsavel = models.EmailField(max_length=100, blank=False, null=False)
    telefone = models.CharField(max_length=15, blank=False, null=False)
    telefone_responsavel = models.CharField(max_length=15, blank=False, null=False)
    unidade = models.ForeignKey(Unidade,on_delete=models.CASCADE,)
    turno = models.ForeignKey(Turno,on_delete=models.CASCADE,)
    serie = models.ForeignKey(Serie,on_delete=models.CASCADE,)
    nivel = models.ForeignKey(Nivel,on_delete=models.CASCADE,)


    def __str__(self):
        return self.nome