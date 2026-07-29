
# Gerencia_tarefa
Repositorio criado para o projeto da aula de métodos ágeis - Semi-presencial

Comandos para subir a aplicação:

# Acessar o projeto caso vc já não esteja nele ainda
cd C:\Users\SEU_USUARIO\Gerencia_tarefa

# Criar o venv (somente na primeira vez)
python -m venv venv

# Ativar o venv
.\venv\Scripts\Activate ou source .venv/bin/activate ou source venv/bin/activate

# Rodar o Backend
python -m uvicorn backend.main:app --reload ou uvicorn backend.main:app --reload

#instalar dependências
pip install fastapi sqlalchemy pydantic streamlit email-validator uvicorn

# Instalar dependências
pip install -r requirements.txt

# Atualizar requirements
pip freeze > requirements.txt

# Abrir o Swagger
http://127.0.0.1:8000/docs

# Rodar o Frontend (ATENÇÃO:novo terminal)
.\venv\Scripts\Activate ou source venv/bin/activate

#subir frontend
streamlit run frontend/app.py

# Executar os testes (novo terminal)
.\venv\Scripts\Activate

#rodar teste
pytest
