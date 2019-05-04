import requests
from rest_framework import serializers
from bs4 import BeautifulSoup
from .models import Cadastro
#request- biblioteca do python que realiza o get da pagina (download deseuselementos)
def webscrape():
    page = requests.get('https://nerdstore.com.br/categoria/especiais/game-of-thrones/')
    soup = BeautifulSoup(page.content, 'html.parser')
#Se odownloadfor realizado é retornado com status 200
#page.status_code
#exibir conteudo da pagina
#page.content
#definicao da div para busca de itens, div que contem os itens desejados.
    itens = soup.find_all('li', class_='product')
#teste para verificar se está trazendo os itens
#print(len(itens))
# for para percorrer a div que contém os itens e capturar os itensdesejados
    for i in itens:
    # buscar pela class
        nome = i.find('h2', class_='woocommerce-loop-product__title')
        link = i.find('a', class_='woocommerce-LoopProduct-link')['href']
        preco = i.find('span', class_='price')
    return nome, link, preco
        #cad = Cadastro()
        #cad.nome = nome
        #cad.link = link
        #cad.preco = preco
        #cad.save()
    #print(nome.text)
    #print(link)
    #print(preco.text)
        #class CadastroSerializer(serializers.ModelSerializer):
         #   class Meta:
          #      model = Cadastro
           #     fields = ('id', 'nome.text', 'link', 'preco.text')
    #print(nome, link, preco)
#print(len(nome, link, preco))
#for nome in nome:
 #   class CadastroSerializer(serializers.ModelSerializer):
  #      class Meta:
   #         model = Cadastro
    #        fields = (len('id', 'nome', 'link', 'preco'))
#class CadastroSerializer(serializers.ModelSerializer):
 #   class Meta:
  #      model = Cadastro
   #     fields = ('id', 'nome', 'link', 'preco')