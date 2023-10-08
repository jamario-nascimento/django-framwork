from django.shortcuts import render


# Criando minha primeira view
def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
    }
    return render(request, 'index.html', context)


def contact(request):
    return render(request, 'contact.html')
