from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('criar/receita', views.cria_receita, name='cria_receita'),
    path('deleta/<int:receita_id>', views.deleta_receita, name='deleta_receita'),
    path('edita/<int:receita_id>', views.edita_receita, name='edita_receita'),
    path('atualiza_receita', views.atualiza_receita, name='atualiza_receita')
]
