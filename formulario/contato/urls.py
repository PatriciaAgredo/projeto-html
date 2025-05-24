from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('sobre/', views.sobre, name='sobre'),
    path('eventos/', views.eventos, name='eventos'),
    path('expositores/', views.expositores, name='expositores'),
    path('galeria/', views.galeria, name='galeria'),
    path('cadastrar/', views.cadastrar_feirante, name='cadastrar_feirante'),
    path('sucesso/', views.sucesso_cadastro, name='sucesso_cadastro'),
]