### Django Project: Jujuba

#### Uma aplicação web escrita em Django que permite que usuários realizem operações CRUD (create, read, update, delete) em recursos de nuvens AWS, Azure e OCI. 

#### A camada de apresentação desta aplicação deve ser uma interface de modelo em estilo Admin Bootstrap. As operações devem ser registradas em um banco de dados MariaDB e devem ser enfileiradas em um RabbitMQ, de modo a permitir que os usuários façam diveras operações e não precisem ficar aguardando o resultado da solicitação da operação. As operações infileiradas devem ser processadas via Python Celery e biblioteca Boto3. Após o processamento, deve ser atualizado no banco de dados o resultado da operação, assim como os seus logs de execução. O usuário solicitante deve ser notificado por e-mail para que ele faça uma consulta no sistema e otenha todos os dados da operação. 

#### A opção do menu esquerdo denomidada "Permissões" deverá possibilitar aos usuários realizarem operações CRUD (create, read, update, delete) de AWS IAM Users, assim como permitir que sejam escolhidos quantos AWS S3 forem necessários para a liberação de permissões de acesso de um AWS IAM User. Também deverá permitir a criação de Access Keys para um AWS IAM User. A opção do menu esquerdo denomidada "Permissões" também deverá permitir que sejam operações CRUD (create, read, update, delete) em AWS IAM Roles, e escolher quantos AWS S3 forem necessários para a liberação de permissões de acesso de uma AWS IAM Role. As AWS IAM roles serão utilizadas em AWS EKS para que uma Kubernetes Service Account vinculada a uma Kubernetes Namespace tenha permissão de acesso em AWS S3 Buckets. 

#### A aplicação web deve possuir autenticação e autorização de usuários via Azure AD. Referente a autorização, as roles de acesso devem ser configuradas via App Roles dentro de uma App Registration do Azure AD. Os usuários deverão ter uma das seguintes roles: no_access (padrão), reader, contributor, administrator. A role "no_access" não permite acesso às opções do menu esquerdo: recursos, permissões, configurações. A role "reader" permite acesso permite acesso em modo leitura (operação CRUD: read) às opções do menu esquerdo: recursos, permissões. A role "contributor" permite acesso em modo escrita (operações CRUD: create, read, update, delete) às opções do menu esquerdo: recursos, permissões. Todo o backend desta aplicação deve ser executada dentro de uma única Namespace de Kubernetes, em quantos Pods forem necessários. 

#### O sistema deve possuir uma opção no menu esquerdo denominada "Configuração", acessível somente para usuários que possuírem a role "administrator". A opção "Configuração" deve permitir a escolha de um "Ambiente" por meio de uma lista suspensa. Conforme a seleção do "Ambiente" deve ser permitido alterar os valores dos campos: Nome do Ambiente, AWS Region (código da região da aws), AWS Account Number (conta da aws em que o recurso reside), AWS EKS Id (id do eks onde o recurso reside), AWS IAM Role (role que o script python deve assumir durante as operações via boto3). 

#### A opçao "Configuração" também deve permitir a inserção de um novo "Ambiente", com os mesmos campos disponíveis. As operações CRUD dentro das opções do menu esquerdo "Recursos" e "Permissões" devem sempre exibir uma lista suspensa para escolha do "Ambiente" em que a operação deverá ser realizada. O nome do "Ambiente" deve definir em qual região da aws, conta da aws e id do eks o recurso será criado. A aplicação irá gerenciar aws bucket s3, aws iam user, aws iam role em diversas regiões e contas da aws, conforme a lista de ambientes. Apenas uma stack da aplicação estará em execução, portanto estará em execução em uma única regiao e conta da aws. 

#### No backend da aplicação não pode ser utilizada nenhuma linguagem interpretada além do python, como por exemplo: node js, typescript. Utilizar sempre venv no python. Utilizar o arquivo "requirements.txt" para realizar instalação de pacotes do python via pip. Incluir sudo nos comandos do shell do linux sempre que necessário. 

#### A role "administrator" deve possuir as mesmas permissões da role "contributor" adicionando acesso a opção de menu "Configuração". Cada "ambiente" deve possuir apenas 1 aws account number, 1 aws region, 1 aws eks id. A aplicação deverá permitir no futuro a gerência de outros tipos de recursos na aws, além de aws bucket s3, desta forma a aplicação deve permitir ao usuário a seleção do tipo de recurso que ele deseja realizar as operações CRUD. A aplicação deve suportar multilinguismo através de um arquivo de tradução de termos. O nome da pasta do projeto django deve ser "project". 

#### O nome da pasta do aplicativo django deve ser "portal". O nome da pasta da workspace do projeto gpt deve ser "jujuba".

### python setup
```bash
# execute commands:
# python virtual environment
python -m venv venv
source venv/bin/activate
# mysqlclient prereqs
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
# django install + requirements
pip install -r requirements.txt
# django project
django-admin startproject project .
# django application
python manage.py startapp portal

```

### kubernetes setup
```bash
# install minikube 
# https://minikube.sigs.k8s.io/docs/start/
# execute commands:
# docker start
sudo /etc/init.d/docker start
# minukube start
minikube start
minikube dashboard
# setup kubernetes resources
kubectl config set-context --current --namespace=jujuba
kubectl apply -f manifests/namespace.yaml
kubectl apply -f manifests/mariadb.yaml
kubectl apply -f manifests/rabbitmq.yaml
kubectl get pods --watch
```

### development setup
```bash
# execute commands:
# allow connection to mariadb from wsl
kubectl expose deployment/mariadb --type=NodePort --port=3306
# wsl test mariadb connection
mysql --host=192.168.49.2 --user=root --password=jujuba --port=32128
> CREATE DATABASE jujuba;
# Query OK, 1 row affected (0.00 sec)

# allow connection to rabbitmq from wsl
kubectl expose deployment/rabbitmq --type=NodePort --port=15672
amqp://admin:jujuba@192.168.49.2:30347/

#allow connection to rabbitmq web management from web browser
minikube service rabbitmq -n jujuba --url
GET http://127.0.0.1:34381
```

### project config
```bash
# edit file: .env
SECRET_KEY="......................."    # value from settings.py
ALLOWED_HOSTS="127.0.0.1,localhost"     # comma separated strings
DATABASE_NAME=jujuba                    # string
DATABASE_USER=root                      # string
DATABASE_PASS=jujuba                    # string
DATABASE_HOST="192.168.49.2"            # ip address or fqdn hostname
DATABASE_PORT=32128                     # numeric
LANGUAGE_CODE="en-us"                   # ISO 639-1 standard language code
TIME_ZONE="America/Sao_Paulo"           # https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
BROKER_URL="amqp://admin:jujuba@192.168.49.2:30347/"    # rabbitmq url format
```

```bash
# edit file: project/settings.py
SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = list(env("ALLOWED_HOSTS").split(","))

TIME_ZONE = env("TIME_ZONE")

LANGUAGE_CODE = env("LANGUAGE_CODE")

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': env("DATABASE_NAME"),
    'USER': env("DATABASE_USER"),
    'PASSWORD': env("DATABASE_PASS"),
    'HOST': env("DATABASE_HOST"),
    'PORT': env("DATABASE_PORT"),
    }
}

AAD_CONFIG = AADConfig.parse_json(file_path='aad.config.json')

BROKER_URL = env("BROKER_URL")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'celery',
    'portal',
]

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'static'

AAD_CONFIG = AADConfig.parse_json(file_path='aad.config.json')

BROKER_URL = env("BROKER_URL")

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
```

### database setup
```bash
# execute commands:
python manage.py migrate
```

### start webserver
```bash
# execute commands:
python manage.py runserver localhost:8000
```

### create models
```bash
# edit file: portal/models.py
class MinhaClasse(models.Model):
    name = models.CharField(max_length=63)    
    def salvar(self):
        self.save()    
    
    def __str__(self) -> str:
        return self.name
```

### create tables for models
```bash
# execute commands:
python manage.py makemigrations portal
python manage.py migrate portal
python manage.py migrate
```

### django admin
```bash
# edit file: portal/admin.py
from django.contrib import admin
from .models import AWS_S3
admin.site.register(AWS_S3)

# start webserver
python manage.py runserver localhost:8000
# open another terminal and execute commands:
source virtualenv/bin/activate
# create portal admin user & password
python manage.py createsuperuser
# open web browser: http://127.0.0.1:8000/admin/
```

### azuread sso
```bash
# https://learn.microsoft.com/en-us/training/modules/msid-django-web-app-sign-in/3-exercise-register-django-web-app

# Microsoft Entra App Registration:
# Redirect URI: http://localhost:8000/auth/redirect
# Generate a secret

# create file aad.config.json
```

```json
{
    "type": {
        "client_type": "CONFIDENTIAL",
        "authority_type": "SINGLE_TENANT",
        "framework": "DJANGO"
    },
    "client": {
        "client_id": "{enter-your-client-id-here}",
        "client_credential": "{enter-your-client-secret-here}",
        "authority": "https://login.microsoftonline.com/{enter-your-tenant-id-here}"
    },
    "auth_request": {
        "redirect_uri": null,
        "scopes": [],
        "response_type": "code"
    },
    "flask": null,
    "django": {
        "id_web_configs": "MS_ID_WEB_CONFIGS",
        "auth_endpoints": {
            "prefix": "auth",
            "sign_in": "sign_in",
            "edit_profile": "edit_profile",
            "redirect": "redirect",
            "sign_out": "sign_out",
            "post_sign_out": "post_sign_out"
        }
    }
}
```

```bash
# edit file settings.py
from ms_identity_web.configuration import AADConfig
from ms_identity_web import IdentityWebPython

AAD_CONFIG = AADConfig.parse_json(file_path='aad.config.json')
MS_IDENTITY_WEB = IdentityWebPython(AAD_CONFIG)
ERROR_TEMPLATE = 'auth/{}.html' # for rendering 401 or other errors from msal_middleware
MIDDLEWARE.append('ms_identity_web.django.middleware.MsalMiddleware')
```

``` bash
# execute command:
python manage.py runserver localhost:8000
```
