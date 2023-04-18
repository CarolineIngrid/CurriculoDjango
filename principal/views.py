from django.shortcuts import render
from .forms import ContatoForm
from django.http import HttpResponse

def Info(request):
    form = ContatoForm()
    context = {
        'form': form
    }
    return render(request, 'principal/index.html', context=context)

# def form_modelform(request):
#     form =
#     return render(request, 'principal/formulario_modelform.html')