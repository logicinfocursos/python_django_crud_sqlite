# crud em django / python - cadastro de produtos

esse projeto é meramente para ilustrar o uso do django/python

# recursos usados:
python:
https://www.python.org/

django:
https://www.djangoproject.com/start/overview/


step by step:
- criar a venv de nome 'venv'
python -m venv venv

- ativar a venv
.\venv\scripts\activate

- instalar o django
pip install django

- criar a pasta do projeto principal (app_main)
django-admin startproject app_main .

- executar o projeto pela primeira vez
python manage.py runserver

- executar a primeira migration
python manage.py migrate

- criar o super user (user: admin / password: admin)
python manage.py createsuperuser

- criar o app principal (app_products)
python manage.py startapp app_products

- inserir a url do app_products na aplicação (./app_main/urls.py)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_products/', include('app_products.urls')),
]

- em app_products, criar um arquivo ./app_products/urls.py:
from django.contrib import admin
from django.urls import path, include
from .views import home

urlpatterns = [
    path('', home),
]

- em ./app_products/views.py, criar a função 'home'
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

- criar o html de home
criar em './app_products/templates/index.html'  

- registrar o projeto 'app_products' em ./app_main/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_products',   <-- adicionar o projeto app_products aqui nessa posição
]

- criar os 'models' do projeto para a criação das tabelas no sqlite em './app_products/models.py':
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

-registrar o model Product em ./app_products/admin.py:
from django.contrib import admin
from .models import Product          <- incluir essa linha

admin.site.register(Product)         <- incluir essa linha

- gerar uma migration com a estrutura da tabela 'Product'
python manage.py makemigrations

- executar a migração (a tabela 'app_products_product' será criada no sqlite):
python manage.py migrate

- para visualizar as tabelas do projeto, instalar a seguinte extensão no visual code:
SQLITE Viewer by Florian Klampfer	

- verificar o resultado em http://127.0.0.1:8000/admin/, em 'app_products' irá aparecer a tabela 'Products'
incluir registros,para ver o funcionamento...

- para que o conteúdo dos campos seja exibido, é necessário criar um método me './app_products/models.py':
inserir logo abaixo da definição dos campos:
from django.db import models

class Product(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):              <- incluir essa linha
        return self.nome            <- incluir essa linha

- para listar os registros da tabela Product, realizar as seguintes alterações no arquivo ./app_products/views.py:
from django.shortcuts import render
from .models import Product          <- incluir essa linha

def home(request):
    _Products = Product.objects.all()
    return render(request, 'index.html',{'Products': _Products})  <- incluir alterada (estamos enviando a variável Products para ser acessado pela view './app_products/templates/index.html')

- preparar o arquivo './app_products/templates/index.html' para receber informações vindas de './app_products/views.py',
vide documentação sobre Django template language:
https://docs.djangoproject.com/en/4.1/ref/templates/language/
