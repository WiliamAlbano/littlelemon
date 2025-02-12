# 🍽️ Little Lemon Restaurant API

This project is a web application developed with Django to manage menus and table reservations for the Little Lemon restaurant.

Este projeto é uma aplicação web desenvolvida com Django para gerenciar menus e reservas de mesas no restaurante Little Lemon.

---

## 📌 Features / Funcionalidades

✅ Serves static HTML content using Django / Servir conteúdo HTML estático com Django  
✅ Project versioned in Git / Projeto versionado no Git  
✅ Connects backend to MySQL database / Conectar o backend a um banco de dados MySQL  
✅ API for menu and table booking / APIs para gerenciamento do menu e reservas de mesas  
✅ User registration and authentication / Registro e autenticação de usuários  
✅ Unit tests included / Contém testes unitários  
✅ API can be tested with Insomnia / API pode ser testada com Insomnia  

---

## 🚀 Technologies Used / Tecnologias Utilizadas

- **Django**: Backend framework  
- **Django REST Framework (DRF)**: RESTful API construction / Construção de APIs RESTful  
- **Djoser**: Authentication and token management / Gerenciamento de autenticação e tokens  
- **MySQL**: Relational database / Banco de dados relacional  
- **Insomnia/Postman**: API testing / Testes das APIs  

---

## ⚙️ Setup / Configuração

### 📌 1. Clone the repository / Clonar o repositório
```bash
git clone https://github.com/WiliamAlbano/littlelemon
cd your-repository
```

### 📌 2. Create and activate a virtual environment / Criar e ativar um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate  # Windows
```

### 📌 3. Install dependencies / Instalar dependências
```bash
pip install -r requirements.txt
```

### 📌 4. Configure the database / Configurar o banco de dados
Edit the `settings.py` file with your MySQL credentials / Edite o arquivo `settings.py` com suas credenciais do MySQL:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon_db',
        'USER': 'your_user',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
Now apply migrations / Agora, aplique as migrações:
```bash
python manage.py migrate
```

### 📌 5. Create a superuser / Criar um superusuário
```bash
python manage.py createsuperuser
```

---

## 🔑 Authentication / Autenticação

### 📌 1. Obtain an authentication token / Obter um token de autenticação
**URL:** `http://127.0.0.1:8000/auth/token/login/`  
**Method / Método:** `POST`  
**Body:**
```json
{
  "username": "your_user",
  "password": "your_password"
}
```
**Expected response / Resposta esperada:**
```json
{
  "auth_token": "your_token_here"
}
```

### 📌 2. Use the token for authentication / Como usar o token para autenticação
For protected endpoints, include the token in the request headers / Para acessar endpoints protegidos, envie o token no cabeçalho:
```
Authorization: Token your_token_here
```

---

## 📌 API Endpoints / Endpoints da API

### 📝 1. Menu
| Method | URL | Description / Descrição |
|--------|-----|----------------|
| GET | `/api/menu-items/` | List menu items / Listar itens do menu |
| GET | `/api/menu-items/<id>/` | Get a specific item / Obter um item específico |
| POST | `/api/menu-items/` | Create a new item (auth required) / Criar um novo item (requer autenticação) |
| PUT | `/api/menu-items/<id>/` | Update an item (auth required) / Atualizar um item (requer autenticação) |
| DELETE | `/api/menu-items/<id>/` | Delete an item (auth required) / Remover um item (requer autenticação) |

### 📅 2. Table Reservations / Reservas de Mesas
| Method | URL | Description / Descrição |
|--------|-----|----------------|
| GET | `/restaurant/booking/tables/` | List reservations / Listar reservas |
| POST | `/restaurant/booking/tables/` | Create a new reservation (auth required) / Criar uma nova reserva (requer autenticação) |

---

## 📌 Testing with Insomnia / Testando com Insomnia

1️⃣ **Open Insomnia**  
2️⃣ **Create a new request** and select **POST**  
3️⃣ **Enter the URL:** `http://127.0.0.1:8000/auth/token/login/`  
4️⃣ **Add the JSON body:**  
   ```json
   {
     "username": "your_user",
     "password": "your_password"
   }
   ```
5️⃣ **Copy the token and use it in future requests**  

---

## 🧪 Running Unit Tests / Executando Testes Unitários
```bash
python manage.py test
```

---

## 📌 How to Contribute / Como Contribuir

1. Fork the repository / Faça um **fork** do repositório  
2. Create a new branch: `git checkout -b my-feature`  
3. Commit changes: `git commit -m 'My new feature'`  
4. Push to GitHub: `git push origin my-feature`  
5. Open a Pull Request / Abra um **Pull Request**  

---

## 📌 Author / Autor
Developed by Wiliam Albano (https://github.com/WiliamAlbano)  
Desenvolvido por Wiliam Albano (https://github.com/WiliamAlbano)

---
