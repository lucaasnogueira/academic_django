from django.urls import path , include, re_path
from .views import( 
    cadastro,
    cadastrados, 
    funcionario_novo,
    funcionario_update,
    funcionario_delete,
)
                    

urlpatterns = [
    re_path('cadastrar/', cadastro, name='funcionario_cadastrar'),
    re_path('cadastrados/', cadastrados, name='funcionario_cadastrado'),
    re_path('funcionario-novo/', funcionario_novo, name='funcionario_novo'),
    re_path('funcionario-update/(?P<id>\d+)/', funcionario_update, name='funcionario_update'),
    re_path('funcionario-delete/(?P<id>\d+)/', funcionario_delete, name='funcionario_delete'),

]