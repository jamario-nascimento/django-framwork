# Criando Projetos Django

Para inicar instalamos o PyCharm IDE para desenvolvimento dem Python.
Criamos um novo projeto chamado django1

### Criando arquivo requirements e instalando Djando admin

```
pip freeze > requirements.txt
pip install django-admin
```
### Inicializando o  djando-amin no projeto

```
django-admin startproject django1 .
```
django1 faz relação ao nome do projeto e o . informa que deve ser criado na raiz do diretório, se remover o . do final ele cria um novo diretório django1/django1

### Inicializando uma nova aplicação
```
django-admin startapp core
```
#### Explicando estrutura
core é o nome da aplicação
diretório migations: pacote responsavel pelas migrações de database
danter init __init__.py
admin.py: configira aplicação para admin Django
apps.py:
models.py: modelos de dados o que vamos permitir na aplicação
views.py: 

### Integrando aplicações ao Projeto
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'core',
]
```
Adicionar em django1 ( projeto) arquivo settings, instaled app o nome dos app

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Adicionar em templates o diretórios onde vão estar os templates da aplicacao

## Driferença entre Projetos Django e Aplicação Django

Projeto é um todo do sistema e aplicações são aplicações plugaveis, você pode criarpedfações de 
suas aplicações para construir um sistema todo. Uma das vantagens é poder copiar um pacote inteiro e jogar em outro projeto fazendo reaproveitamento
de modulos e blocos de código.

## Padrão MTV Django

usuário -> browser -> templates, URLS -> views -> models -> database

M = Models
T = Templates
V = Views

Django views funciona como camada controller do MVC.


## Comandos django devem ser executados no diretorio no manage.py

rodando aplicação - porta padrao =http://127.0.0.1:8000/
```
python manage.py runserver
```
## Views

criamos views nas aplicacçoes como um função python views.py

```
def index(request):
    return render(request, 'index.html')
    
```

## Rotas

O urls.py vem por padrão no projeto e não na aplicação
uma forma de fazer é importar no projeto django1 -> urls.py a view da aplicação core

```
from django.contrib import admin
from django.urls import path
from core.views import  index,contact
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('contact', contact),
]
```
Mas não é ideal ter arquivo de rotas no projeto, e sim criar as rotas na aplicação

ficando assim a importação de core no projeto
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

```
Depois é só criar um arquivo urls.py na aplicação.
Importar o django.urls e as vies do meu app

````
from django.urls import path
from  .views import  index, contact

urlpatterns = [
    path('', index),
    path('contact', contact)
]
````
## Models

Criando uma classe model Python
```
from django.db import models

# Create your models here.
 class Produto(models.Model):
     nome = models.CharField('Nome', max_length=100)
     preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
     estoque = models.IntegerField('Quantidade em Estoque')
```
Criando uma migrations

```
python manage.py makemigrations
```
Ao final recebomos uma mensagem mais ou menos assim
'$ python manage.py makemigrations
Migrations for 'core':
  core\migrations\0001_initial.py
    - Create model Produto'

Rodando uma migrations

```
python manage.py migrate
```

## Admin Django

criando super usuário
```
python manage.py createsuperuser
```
No admin.py deve ser registrados os modulos

## Django shell

```
python manage.py shell

```
### Como interagir em um model via shell

```
python manage.py shell
from core.models import Product
dir(Product)
```
Neste comando acima inicializamos o paython shell, depois importamos
nosso app 'core' e o model 'Product' e importamos. A função dir vai retornar tudo que esse model tem.

```
dir(Product.objects)
products = Product.objects.all()
products
```

Aqui listamos o atributo objects do Model depois instanciamos o Product com o objects e o métoddo all
depois escrevendo somente o nome do nosso objeto instanciado temos essa resposta "<QuerySet [<Product: PS1>]>"

```
for product in products: 
  print(product)
```
## Arquivos estáticos

Criar um diretório chamado static dentro do app, depois criar seus diretorios ex:
.css
.js
.images

No arquivo settings dentro do projeto informar as variáveis o:
STATIC_URL = usado para acessar em desenvolvimento
STATIC_ROOT = usado para acessar em produção

Comando para copiar os arquivos estáticos de desenvolvimento para produção
```
python manage.py collectstatic
```

## Tratamento erro objeto não encontrado

Neste exemplo no arquivo de views importamos essa funcionalidade do módulo MVC,
alterando a criação do objeto chamamos esse método get_object_or_404 e passamos a classe e a chave no caso id.

```
from django.shortcuts import get_object_or_404

def product(request, pk):
    productItem = get_object_or_404(Product, id=pk)
    context = {
        'product': productItem
    }
    return render(request, 'product.html', context)
```

### Tratando 404 

  Ir ao projeto e no arquivo urls.py importar os handles e o app que deseja tratar 
  ```
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = views.error404
```