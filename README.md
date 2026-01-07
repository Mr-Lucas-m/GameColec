# 🎮 GameColec API

API RESTful para gerenciamento de **coleção de games e consoles**, com autenticação JWT, controle de permissões por role (admin/user), testes automatizados e arquitetura modular baseada em boas práticas profissionais.

---

## 📌 Visão Geral

A **GameColec API** permite:

* Cadastro e autenticação de usuários
* Controle de acesso por perfil (**admin** e **user**)
* Cadastro de consoles (somente admin)
* Cadastro de games vinculados a consoles (somente admin)
* Consulta de games por console


---

## 🏗️ Arquitetura do Projeto

```text
├── app
│ ├── api
│ │ └── v1
│ │ └── api_router.py
│ ├── core
│ │ ├── __init__.py
│ │ ├── config.py # Configurações e variáveis de ambiente
│ │ ├── database.py # Conexão e sessão do banco
│ │ ├── dependencies.py # Dependências globais (auth, roles)
│ │ └── security.py # JWT, hash de senha
│ ├── modules
│ │ ├── auth
│ │ │ ├── auth_router.py
│ │ │ └── auth_service.py
│ │ ├── console
│ │ │ ├── console_model.py
│ │ │ ├── console_router.py
│ │ │ ├── console_schema.py
│ │ │ └── console_service.py
│ │ ├── game
│ │ │ ├── game_model.py
│ │ │ ├── game_router.py
│ │ │ ├── game_schema.py
│ │ │ └── game_service.py
│ │ └── user
│ │ ├── user_model.py
│ │ ├── user_router.py
│ │ ├── user_schema.py
│ │ └── user_service.py
│ └── main.py
├── tests
│ ├── conftest.py
│ ├── test_auth.py
│ ├── test_console.py
│ └── test_game.py
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

### 📐 Padrões Utilizados

* Arquitetura modular por domínio
* Separação clara entre:

  * **Router** (camada HTTP)
  * **Service** (regras de negócio)
  * **Model** (ORM)
  * **Schema** (validação e contrato)
* Dependency Injection (FastAPI)

---

## 🔐 Autenticação & Segurança

* Autenticação via **JWT (Bearer Token)**
* Senhas criptografadas com **bcrypt**
* Controle de permissões por role:

| Role  | Permissões             |
| ----- | ---------------------- |
| user  | Apenas leitura         |
| admin | Criar consoles e games |

Exemplo de Header:

```http
Authorization: Bearer <TOKEN_JWT>
```

---

## 🚀 Tecnologias Utilizadas

* **Python 3.13**
* **FastAPI**
* **SQLAlchemy**
* **PostgreSQL** (compatível com SQLite para testes)
* **Pydantic v2**
* **JWT (python-jose)**
* **Pytest**

---

## 📦 Instalação e Execução

### 1️⃣ Clone o projeto

```bash
git clone https://github.com/seu-usuario/gamecolec.git
cd gamecolec
```

### 2️⃣ Crie o ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instale as dependências

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure o `.env`

```env
DATABASE_URL=postgresql://user:password@localhost:5432/gamecolec
SECRET_KEY=super-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

### 5️⃣ Execute a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 🧪 Testes Automatizados

O projeto possui **testes de integração completos**, cobrindo todo o fluxo real da API.

### Executar testes:

```bash
pytest -v
```

### Fluxos testados:

* Login válido e inválido
* Criação de console (admin)
* Bloqueio de criação (user)
* Criação de game (admin)
* Listagem de games por console

---

## 🔄 Fluxo de Uso da API

1️⃣ Registrar usuário

```http
POST /api/v1/auth/register
```

2️⃣ Login (gera token)

```http
POST /api/v1/auth/login
```

3️⃣ Criar console (admin)

```http
POST /api/v1/consoles
```

4️⃣ Criar game (admin)

```http
POST /api/v1/games
```

5️⃣ Listar games por console

```http
GET /api/v1/games/consoles/{console_id}
```

---

## 📄 Documentação Automática

Acesse:

* Swagger UI → `http://localhost:8000/docs`
* ReDoc → `http://localhost:8000/redoc`

---

## 🧠 Aprendizados Demonstrados

* JWT na prática
* Role Based Access Control (RBAC)
* Testes com FastAPI + Pytest
* Arquitetura escalável
* Padrões profissionais de API

---

## 👨‍💻 Autor

**Lucas Marques**
Backend Developer • Python • FastAPI

---

## ⭐ Considerações Finais

Este projeto foi desenvolvido com foco em **qualidade, organização e práticas reais de mercado**, sendo totalmente extensível para novas funcionalidades como:

* Favoritos
* Avaliações
* Upload de imagens
* Paginação e filtros

🚀
