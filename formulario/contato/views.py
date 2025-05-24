from django.shortcuts import render, redirect
from .forms import CadastroFeiranteForm

def cadastrar_feirante(request):
    if request.method == 'POST':
        form = CadastroFeiranteForm(request.POST)
        if form.is_valid():
            form.save()
           
            return redirect('sucesso_cadastro')
    
    else: 
        form = CadastroFeiranteForm() 

   
    return render(request, 'contato/cadastro_feirante.html', {'form': form})


def sucesso_cadastro(request):
    return render(request, 'contato/sucesso_cadastro.html')
def index(request):
    return render(request, 'contato/index.html')
def eventos(request):
    return render(request, 'contato/eventos.html')
def expositores(request):
    return render(request, 'contato/expositores.html')
def galeria(request):
    return render(request, 'contato/galeria.html')
def sobre(request):
    return render(request, 'contato/sobre.html')
