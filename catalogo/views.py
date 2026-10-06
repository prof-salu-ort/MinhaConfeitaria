# catalogo/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Bolo
from .forms import BoloForm

def pagina_inicial(request):
    return render(request, 'catalogo/index.html')

def lista_bolos(request):
    #Busca todos os bolos no banco de dados
    bolos = Bolo.objects.all()
    #Devolve a pagina de listagem de bolos
    #Com o dicionario bolos
    return render(request,
                  'catalogo/lista_bolos.html',
                  {'bolos' : bolos})

def novo_bolo(request):
    if request.method == 'POST':
        form = BoloForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('catalogo:lista_bolos')
    else:
        form = BoloForm()

    return render(request,
                   'catalogo/bolo_form.html',
                   {'form' : form})


def detalhe_bolo(request, pk):
    # 1. Os Detalhes do Bolo
    bolo = get_object_or_404(Bolo, pk=pk)
    return render(request, 'catalogo/detalhe_bolo.html', {'bolo': bolo})


def editar_bolo(request, pk):
    # 2. Atualização do Estoque
    bolo = get_object_or_404(Bolo, pk=pk)

    if request.method == 'POST':
        form = BoloForm(request.POST, request.FILES, instance=bolo)
        if form.is_valid():
            form.save()
            return redirect('catalogo:detalhe_bolo', pk=bolo.pk)
    else:
        form = BoloForm(instance=bolo)

    return render(request, 'catalogo/bolo_form.html', {'form': form})


def apagar_bolo(request, pk):
    # 3. Fim de Linha (Excluir)
    bolo = get_object_or_404(Bolo, pk=pk)

    if request.method == 'POST':
        bolo.delete()
        return redirect('catalogo:lista_bolos')

    return render(request, 'catalogo/bolo_confirmar_exclusao.html', {'bolo': bolo})