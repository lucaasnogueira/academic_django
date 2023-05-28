from django.urls import path , include, re_path
from .views import( 
    cadastro,
    cadastrados, 
    aluno_novo,
    aluno_update,
    aluno_delete,
)
                    

urlpatterns = [
    re_path('cadastrar/', cadastro, name='aluno_cadastrar'),
    re_path('cadastrados/', cadastrados, name='aluno_cadastrado'),
    re_path('aluno-novo/', aluno_novo, name='aluno_novo'),
    re_path('aluno-update/(?P<id>\d+)/', aluno_update, name='aluno_update'),
    re_path('aluno-delete/(?P<id>\d+)/', aluno_delete, name='aluno_delete'),

]