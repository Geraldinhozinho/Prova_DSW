from django.shortcuts import render

# Create your views here.


def Index(request):
    return render(request, 'jogos/index.html')

def Equipe(request):
    return render(request, 'jogos/equipe.html')

def Modalidade(request):
    return render(request, 'jogos/modalidade.html')