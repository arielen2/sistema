from django.shortcuts import render, redirect
from .models import Carro

def criar_carro(request):
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        marca = request.POST.get('marca')
        cor = request.POST.get('cor')
        placa = request.POST.get('placa')

        print(modelo)

        carro = Carro(modelo=modelo, marca=marca, placa=placa, cor=cor)
        carro.save()

        return redirect('form_carro')#redirecionamento para uma rota apos o salvamento
    
    else:
        return render(request, 'main\index.html')