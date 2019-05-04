from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import Cadastro
from .serializer import CadastroSerializer
from bs4 import BeautifulSoup
import requests
from .webscrapping import webscrape
#Home- Pagina inicial exibindo a listagem dos itens.
def home(request):
    cadastros = Cadastro.objects.all()
    return render(request, 'home.html', {'cadastros': cadastros})
#busca dos itens do cadastro no banco de dado
class CadastroViewSet(viewsets.ModelViewSet):
    queryset = Cadastro.objects.all()
    serializer_class = CadastroSerializer
#class lista_itens():
    #cadastro = Cadastro.objects,all()
    #render(, 'home.html', {'cadastro': cadastro})
def add(request):
    page = requests.get('https://nerdstore.com.br/categoria/especiais/game-of-thrones/')
    soup = BeautifulSoup(page.content, 'html.parser')
    # Se odownloadfor realizado é retornado com status 200
    # page.status_code
    # exibir conteudo da pagina
    # page.content
    # definicao da div para busca de itens, div que contem os itens desejados.
    itens = soup.find_all('li', class_='product')
    # teste para verificar se está trazendo os itens
    # print(len(itens))
    # for para percorrer a div que contém os itens e capturar os itensdesejados
    for i in itens:
        # buscar pela class
        nome = i.find('h2', class_='woocommerce-loop-product__title').text
        link = i.find('a', class_='woocommerce-LoopProduct-link')['href']
        preco = i.find('span', class_='woocommerce-Price-amount amount').text
        cad = Cadastro()
        cad.nome = nome
        cad.link = link
        cad.preco = preco
        cad.save()
    #adiciona = CadastroSerializer(request.webscrape() or None)
    #adiciona.save()
    cadastros = Cadastro.objects.all()
    return render(request, 'home.html', {'cadastros': cadastros})