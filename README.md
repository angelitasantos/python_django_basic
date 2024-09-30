### Projeto Grupo Pleno - Python Django


#### variáveis de ambiente (criar)
- Criar os arquivos .env e .gitignore na pasta raiz

#### ambiente virtual (criar/ativar)
##### windows
- python -m venv venv
- venv\Scripts\Activate

##### linux
- python3 -m venv venv
- source venv/bin/activate

#### bibliotecas (instalar)
- python.exe -m pip install --upgrade pip
- pip install django
- pip install pillow
- pip install python-dotenv

requirements (criar)
- pip freeze
- pip freeze > requirements.txt

#### projeto na pasta raiz (iniciar)
- django-admin startproject setup .
- retirar a SECRET_KEY do arquivo settings.py e incluir no arquivo .env
    file: settings.py<br>
        - from pathlib import Path, os<br>
        - from dotenv import load_dotenv<br>
        - load_dotenv()<br>
        - SECRET_KEY = str(os.getenv('SECRET_KEY'))<br>
    file: .env<br>
        - SECRET_KEY = chave<br>
- python manage.py runserver
