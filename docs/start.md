# Start

### libs

virtualenv env
cd env/Scripts
.\activate
cd ../..

pip install django
pip install django-filter
pip install markdown
pip install djangorestframework
pip install mysqlclient
pip install mysql-python

pode ser usado assim: pip install django mysqlclient


django-admin startproject archive_api .
django-admin startapp person  

python manage.py migrate # tem que subir umonte de tabelas
python manage.py createsuperuser

pip freeze > requirements.txt

## Configurar banco

https://www.codigofluente.com.br/configurando-o-django-com-mysql-windows/

## setting.py

Colocamos americaSP em tempo

INSTALED APPS:
'django_filters',
'rest_framework',
'person'

e embaixo de static
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')




## Feito models.py

## Depois coloca as tabelas em admin para fazer harcode no admin

admim.py

## DJANGO REST FRAMEWORK (DRF)

Criamos :

serializer.py

view.py

e temos que usar rotuer para mapear viewsset:

mexe em project/urls.py

### Mudar formato de Daa do serializer

originalmente vem assim

DRF: 2018-12-21T19:17:59.353368Z
Model field: 2018-12-21T19:17:59.353368+00:00


em settings.py


REST_FRAMEWORK = {
    ...
    'DATETIME_FORMAT': "%Y-%m-%d - %H:%M:%S", 
    ...
}

## CORS

Para acessar a API precisa do Cors, e, todas as requisiçôes tem que temrinar em '/' para funcionar corretamente

## ManyToMany Nested

Usa-se uma lib diferente para os serializers.

## Django Env (`django-environ`)

`pip install django-environ`

Gerencia Ambiente no Django

