# Prova_DSW
Prova de Desenvolvimento WEB



Crie um ambiente virtual dentro da pasta do repositório
python -m venv venv

ative o ambiente
.\venv\Scripts\activate

instale o django no ambiente virtual ja ativo
pip install django

gere as migrações e envie elas para o banco
python manage.py makemigrations
python manage.py migrate

crie um super úsuario
python manage.py createsuperuser

cadastre informações nas tabelas e retorne a rota raiz:

http://127.0.0.1:8000

fluxo alternativo:

Crie um ambiente virtual dentro da pasta do repositório
python -m venv venv

ative o ambiente
.\venv\Scripts\activate

execute
pip freeze -r requirements.txt

crie um super úsuario
python manage.py createsuperuser

cadastre informações nas tabelas e retorne a rota raiz:

http://127.0.0.1:8000