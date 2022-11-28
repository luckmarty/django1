from django.shortcuts import render, get_object_or_404
from .models import Produto
from  django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Django é massa, veio!',
        'produtos': produtos,
    }
    return render(request, 'index.html', context)


def contato(request):
    return render(request, 'contato.html')


def produto(request, pk):
    # produto = Produto.objects.get(pk=pk)
    produto = get_object_or_404(Produto, pk=pk)
    context = {
        'produto': produto,
    }
    return render(request, 'produto.html', context)


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(), content_type='text/html; charset=utf8', status=500)
