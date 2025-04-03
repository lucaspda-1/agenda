Iniciar o projeto Django
```bash
python -m venv venv
. venv/bin/activate
pip install django
django-admin startproject project .
python manage.py startapp contact
```
Configurar o Git
```bash
git config --global user.name 'Seu nome'
git config --global user.email 'seu_email@gmail.com'
git config --global init.defaultBranch main
```
Configurar o .gitignore
```bash
git init
git add .
git commit -m 'Mensagem'
git remote add origin URL_DO_GIT
```
Migrando a base de dados do Django
```bash
python manage.py makemigrations
python manage.py migrate
```
Criando e modificando a senha de um superusuário Django
```bash
python manage.py createsuperuser
python manage.py changepassword USERNAME
```
