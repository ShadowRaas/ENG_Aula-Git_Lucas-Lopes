# ENG_Aula-Git_Lucas-Lopes

# Criar Secret Keys:
- Na shell:
'''
python
import secrets
secrets.token_urlsafe(32)
'''
(Após receber a key, copiar e colar a mesma na aba secrets do replit, usando como key: 'SECRET_KEY' e como value a key recebida))

# Iniciar o seu App:
- No console:
'''
python3 manage.py startapp nome_do_seu_app
'''

# Fazer migrações:
- Na shell:
"""
python manage.py makemigrations
python manage.py migrate
"""

# Criar Super User:
- Na shell:
'''
python manage.py createsuperuser
#Colocar o nome do super user (eg. admin), seu email e senha)
'''

# Adicionar o projeto do Replit no GitHub:
- Baixar Git for windows
 https://gitforwindows.org
- Baixar o zip do seu projeto no Replit
- Abrir PowerShell no seu computador windows
(verifique se o git for windows realmente foi instalado antes de usar o PowerShell)
- Antes de começar a usar o Git, é importante configurar seu nome de usuário e endereço de e-mail. No PowerShell, execute os seguintes comandos, substituindo "seu_nome" pelo seu nome e "seu_email" pelo seu endereço de e-mail do GitHub:
'''
git config --global user.name "seu_nome"
git config --global user.email "seu_email"
'''
- No PowerShell, navegue para o diretório onde você deseja clonar o repositório do GitHub. Por exemplo, para clonar o repositório em uma pasta chamada "meu_projeto", use o seguinte comando:
'''
cd ~/Diretorio_escolhido
git clone https://github.com/seu_usuario/nome_do_repositorio.git meu_projeto
'''
(Substitua "seu_usuario" pelo seu nome de usuário do GitHub e "nome_do_repositorio" pelo nome do repositório no GitHub.)
- No Windows Explorer, copie a pasta que você deseja adicionar ao repositório Git. Em seguida, volte para o PowerShell.
- No PowerShell, execute os seguintes comandos para adicionar a pasta ao controle de versão do Git:
'''
cd ~/Diretorio_escolhido/meu_projeto
git add .
git commit -m "Adicionar pasta inicial"
''' 
- No PowerShell, envie as alterações para o GitHub usando o comando 'git push':
'''
git push
'''
(Se for solicitado, faça login na sua conta do GitHub para terminar o processo)
