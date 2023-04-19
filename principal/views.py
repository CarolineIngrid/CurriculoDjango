from django.shortcuts import render
from .forms import ContatoForm
from .models import Contato
from django.views.decorators.csrf import csrf_protect

@csrf_protect
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
            contato = Contato.objects.filter()
            contato.status = True
            contato = form.save()
            form = ContatoForm()

        context = {
        'form': form
    }
    return render(request, 'principal/index.html', context=context)



# def form_modelform(request):
#     form =
#     return render(request, 'principal/formulario_modelform.html')