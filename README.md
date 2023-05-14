# ENG_Aula-Git_Lucas-Lopes

# Criar Secret Keys:
-Na shell:
'''
python
import secrets
secrets.token_urlsafe(32)
'''
(Após receber a key, copiar e colar a mesma na aba secrets do replit, usando como key: 'SECRET_KEY' e como value a key recebida))

# Iniciar o seu App:
-No console:
'''
python3 manage.py startapp nome_do_seu_app
'''

# Fazer migrações
-Na shell:
"""
python manage.py makemigrations
python manage.py migrate
"""

# Criar Super User
-Na shell:
'''
python manage.py createsuperuser
#Colocar o nome do super user (eg. admin), seu email e senha)
'''
