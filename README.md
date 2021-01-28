# README #

# Sistema de gestão dos dados históricos das olimpiadas disponíveis em: 
 - https://www.kaggle.com/heesoo37/120-years-of-olympic-history-athletes-and-results#athlete_events.csv

## Esta é uma API simples para:

* avaliação no processo seletivo da Celero (https://celero.com.br/)
* criar uma interface unificada para gerenciar os dados dos ganhadores de medalhas nas olimpiadas
* os administradores podem fazer o login e gerenciar todos através da interface de administração do Django

## Executando localmente

1. Deve ter Python 3.X e Postgres versão 12.x instalado e em execução
1. Clone o repositório e faça cd na pasta criada
1. Crie um ambiente virtual: `python -m venv venv`
1. Vá para o seu ambiente virtual: `source venv/bin/activate`
1. Instale as dependências: `pip install -r requirements.txt`
1. Crie um usuário administrador para fazer login na interface de administração do Django: `python manage.py makesuperuser`
1. Configurar banco de dados
     1. Crie o banco de dados: `CREATE DATABASE api_desafio_celero;`
     1. Crie o usuário do banco de dados: `CREATE USER admin`;
     1. Conceda privilégios ao usuário para nosso banco de dados;
     1. Execute migrações: `python manage.py migrate`
1. Execute o aplicativo: `python manage.py runserver`
1. Visualize a API em `localhost:8000/historia_olimpica/athlete_events` ou `localhost:8000/historia_olimpica/noc_regions` e a interface admin em` localhost:8000/admin`

## Tabelas 
* historia_olimpica_nocregions
    * noc
    * region
    * notes
* historia_olimpica_athleteevents
    * name
    * sex
    * age
    * height
    * weight
    * team
    * games
    * year
    * season
    * city
    * sport
    * event
    * medal
    * noc_id
    
## API

**Prefix:** /historia_olimpica

**/noc_regions**

* get 
* post
    * Exemplo:
    ```json
    {
        "id": 1,
        "noc": "teste",
        "region": "teste",
        "notes": "teste"
    }
    ```
**/noc_regions/:id**

* get
* patch
* delete

**/athlete_events**

* get 
* post

**/athlete_events/:id**

* get
* patch
* delete