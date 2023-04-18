from django.shortcuts import render
from .forms import ContatoForm
from django.http import HttpResponse

def Info(request):
    if request.method == "GET":
        form = ContatoForm()
        context = {
            'form': form
        }
        return render(request, 'principal/index.html', context=context)
    else:
        form = ContatoForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            form = ContatoForm()
        else:
            context = {
            'form': form
        }
            return render(request, 'principal/index.html', context=context)



# def form_modelform(request):
#     form =
#     return render(request, 'principal/formulario_modelform.html')