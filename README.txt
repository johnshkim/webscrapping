SuperLogin: john
senha: 123

Efetuaei a instalacao do virtuallenv e do django. 
Efetuei a instalacao dasbibliotecas solicitadas no site do django, requests, bs4. 
Template - Home.html.
WebScrapping dentro de views.py

Template Home definido como padrao de url. Podendo acessar pelo http://localhost:8000
Para realizar o webScrapping é necessário acessar: http://localhost:8000/add
Após a adicao no banco será listado nome, link e preco dos itens. 
Utilizado o arquivo urls.py para definicao de urls-> api\core\urls

criei na model o nome, preco e link. 
no arquivo webscrapping está sendo realizado a captura da pagina pelo requests.get, e o armazenamento pelo Cadastroserializer.
A captura do nome, link e preco está sendo realizado pelo soup.find_all
o serializer está realizando o post 
a view está com o padrao do django

Os arquivos estao dentro de desafio->api->core. 
O WebScrapping está dentro de api\core\views.py
05/05/2019- Realizei a devida formatacao dos campos, para ser exibido apenas o nome(titulo), link e preco. 
adicionei o soup.find.all para armazenar todas as li em itens. 
utilizei um for para percorrer os itens e armazenar os nomes(h2, classe- woocommerce-loop-product__title), link (a, classe- oocommerce-LoopProduct-link' armazenando o href)
preco (span, classe- priece) 
utilizei os comandos
print(nome.text)
print(link)
print(preco.text)
para a realizacao de teste pelo cmd. 

Template Home definido como padrao de url. Podendo acessar pelo http://localhost:8000
Para realizar o webScrapping é necessário acessar: http://localhost:8000/add
Após a adicao no banco será listado nome, link e preco dos itens. 
Utilizado o arquivo urls.py para definicao de urls-> api\core\urls

Qualquer duvida ou observacao por favor entrar em contato: 
john sung hwan kim
jshk@hotmail.com
61-992204198 
