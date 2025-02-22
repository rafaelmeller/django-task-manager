<h1 align="center" style="font-weight: bold;">Task Manager API</h1>

<div align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white&style=for-the-badge" alt="Python Badge">
  <img src="https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white&style=for-the-badge" alt="Django Badge">
</div>

#

_Outras versões:_
[_Click here for English_](./README.md)

<h4 align="center"> 
     Status: Completo
</h4>

<p align="center">
 <a href="#sobre-ℹ️">Sobre</a> •
 <a href="#funcionalidades-💻">Funcionalidades</a> •
 <a href="#arquitetura-da-aplicação-🏗️">Arquitetura da Aplicação</a> •
 <a href="#endpoints-da-api-📍">Endpoints da API</a> •
 <a href="#exemplos-de-uso-🖥️">Exemplos de Uso</a> •
 <a href="#configuração-⚙️">Configuração</a> •  
 <a href="#autor-👨🏻‍💻">Autor</a> • 
 <a href="#licença-📝">Licença</a>
</p>

## Sobre ℹ️
Este projeto é um **exercício de aprendizado pessoal**, focado no desenvolvimento de uma **API REST com Django**, aplicando boas práticas como **paginação, filtragem, pesquisa e autenticação OAuth2**.

A API permite que os usuários **gerenciem tarefas**, incluindo:
- Criar, atualizar, visualizar e excluir tarefas.
- Filtrar tarefas por prioridade, status e prazo.
- Pesquisar tarefas por título ou descrição.
- Autenticação de usuários usando **OAuth2 (token-based authentication)**.

Além disso, um script auxiliar (`helper_functions.py`, localizado no diretório `script_examples`) fornece **exemplos de interações com a API via Python**, demonstrando como fazer requisições autenticadas para consultar e gerenciar tarefas através de scripts.

#

## Funcionalidades 💻
- **Autenticação OAuth2**: Acesso seguro à API usando autenticação baseada em tokens.
- **Endpoints para gerenciamento de tarefas**: Suporte completo a operações CRUD (Criar, Ler, Atualizar, Excluir).
- **Filtragem e Pesquisa**: Consulta de tarefas por prioridade, status, prazo e pesquisa textual.
- **Paginação**: Manipulação eficiente de grandes volumes de dados.

#

## Arquitetura da Aplicação 🏗️

A Task Manager API foi construída com Django e Django REST Framework, seguindo uma arquitetura modular composta pelos seguintes componentes:

- **Models**: Define a estrutura das tabelas do banco de dados. O modelo principal, `Task`, inclui campos como título, descrição, prioridade, prazo, status e usuário associado.
- **Serializers**: Converte instâncias dos modelos para JSON e valida os dados recebidos.
- **Views**: Contém a lógica de negócio e interage com os modelos e serializers. As principais views incluem criação, recuperação, atualização e exclusão de tarefas, além do registro de usuários.
- **URLs**: Responsáveis por direcionar as requisições HTTP para as views apropriadas.
- **Autenticação**: Implementação de OAuth2 para garantir autenticação e autorização seguras.

### Fluxo de Dados

1. **Registro de Usuário**: Usuários podem se registrar fornecendo nome de usuário e senha.
2. **Autenticação**: Usuários autenticam-se com suas credenciais para obter um token de acesso.
3. **Gerenciamento de Tarefas**: Usuários autenticados podem criar, visualizar, atualizar e excluir tarefas.

#

## Endpoints da API 📍

A API conta com os seguintes endpoints para manipulação das tarefas:

| Rota                 | Descrição                                          
|----------------------|-----------------------------------------------------
| <kbd>POST /register/</kbd>     | Registra usuários (nome de usuário e senha) [detalhes](#registrar-usuario)
| <kbd>POST /o/token/</kbd>     | Solicita um token de acesso para um usuário [detalhes](#solicitar-token)
| <kbd>POST /api/tasks/</kbd>     | Cria uma nova tarefa para o usuário [detalhes](#criar-tarefa)
| <kbd>GET /api/tasks/</kbd>     | Obtém todas as tarefas do usuário [detalhes](#listar-tarefas)
| <kbd>GET /api/tasks/?param=value</kbd>     | filtra tarefas utilizando um ou mais parâmetros [details](#filtrar-tarefas)
| <kbd>GET /api/tasks/{id}/</kbd>     | Obtém uma tarefa específica pelo ID [detalhes](#buscar-tarefa)
| <kbd>PUT /api/tasks/{id}/</kbd>     | Atualiza uma tarefa pelo ID [detalhes](#atualizar-tarefa)
| <kbd>DELETE /api/tasks/{id}/</kbd>     | Exclui uma tarefa pelo ID [detalhes](#deletar-tarefa)

#

<h3 id="registrar-usuario">POST /register/</h3>

**REQUEST:**

***Data***
```json
{
  "username": "desired-username-here",
  "password": "desired-password-here"
}
```

**RESPONSE (201):**
```json
{"message": "User created successfully"}
```

#

<h3 id="solicitar-token">POST /o/token/</h3>

**REQUEST:**

***Data***
```json
{
  "grant_type": "password",
  "username": "your-username-here",
  "password": "your-password-here",
  "client_id": "your-client-id-here",
  "client_secret": "your-client-secret-here"
}
```

**RESPONSE (201):**
```json
{
  "access_token": "9Lcvhiy108thwJzjTSdyisWMv06XsM", 
  "expires_in": 36000, 
  "token_type": "Bearer", 
  "scope": "read write", 
  "refresh_token": "QY8MHHiNaK7JzsXqzuo5YKt3dBckjI"
}
```

#

<h3 id="criar-tarefa">POST /api/tasks/</h3>

**REQUEST:** <h4 id="post-request"></h4>

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

***Data***
```json
{
  "title": "New Task",
  "description": "This is another task",
  "priority": "Low",
  "deadline": "2021-12-31",
  "status": "Pending",
}
```

**RESPONSE (200):** <h4 id="post-response"></h4>
```json
{
  "id": 2,
  "title": "New Task",
  "description": "This is another task",
  "priority": "Low",
  "deadline": "2021-12-31",
  "status": "Pending",
  "created_at": "2025-02-15T11:49:44.762223Z",
  "updated_at": "2025-02-15T11:49:44.762251Z",
  "user": 4
}
```

#

<h3 id="listar-tarefas">GET /api/tasks/</h3>

**REQUEST:** <h4 id="get-request"></h4>

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

**RESPONSE (200):** <h4 id="get-response"></h4>
```json
{
  "count": 3,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": 1,
      "title": "New Task",
      "description": "This is a new task",
      "priority": "Low",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-15T11:44:35.155255Z",
      "updated_at": "2025-02-15T11:44:35.155284Z",
      "user": 2
    },
    {
      "id": 2,
      "title": "New Task",
      "description": "This is another task",
      "priority": "Low",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-15T11:49:44.762223Z",
      "updated_at": "2025-02-15T11:49:44.762251Z",
      "user": 2
    },
    {
      "id": 3,
      "title": "New Task",
      "description": "This is another new task",
      "priority": "High",
      "deadline": "2021-12-31",
      "status": "Pending",
      "created_at": "2025-02-16T11:17:00.685599Z",
      "updated_at": "2025-02-16T11:17:00.685657Z",
      "user": 2
    }
  ]
}
```

#

<h3 id="filtrar-tarefas">GET /api/tasks/?param=value</h3>

**REQUEST:**

***Headers***
```json
{
  "Authorization": "Bearer your-access-token-here"
}
```

**Query Parameters**
| Parameter          | Type                 | Description                                          
|-----------|---------------|--------------------------------------
search | str | Busca por tarefas com palavras-chave no títulos ou descrição
priority | str | Filtra por prioridade (Low, Medium, High)
status | str | Filtra por status (Pending, Completed)
deadline | date |	Filtra as tarefas por data limite (YYYY-MM-DD format)

**Exemplos de Request URL:**

#### ```GET /api/tasks/?search=payment```
#### ```GET /api/tasks/?priority=High```
#### ```GET /api/tasks/?status=Pending```
#### ```GET /api/tasks/?deadline=2025-05-01```
#### ```GET /api/tasks/?priority=High&status=Pending&deadline=2025-05-01```

#### Nota: Todos parâmetros são opcionais, é possível fornecer múltiplos ou nenhum.

**RESPONSE (200):**

Segue o mesmo padrão de resposta de [GET](#get-response)

#

<h3 id="buscar-tarefa">GET /api/tasks/{id}/</h3>

**REQUEST:**

Segue o mesmo padrão de resposta de [GET](#get-request)

**RESPONSE(200):**

Segue o mesmo padrão de resposta de [POST](#post-response)

#

<h3 id="atualizar-task">PUT /api/tasks/{id}/</h3>

**REQUEST:**

Segue o mesmo padrão de [POST](#post-request)

**RESPONSE (200):**

Segue o mesmo padrão de resposta de [POST](#post-response)

#

<h3 id="deletar-task">DELETE /api/tasks/{id}/</h3>

**REQUEST:**

Segue o mesmo padrão de [GET](#get-request)

**RESPONSE (204):**

Não há conteúdo na resposta.

#

## Exemplos de Uso 🖥️

Caso necessite de exemplos práticos de como interagir com a API usando scripts em Python, consulte os seguintes arquivos no diretório `script_examples`:

- **`helper_functions.py`** – Contém funções para realizar operações CRUD nas tarefas.  
- **`example_add_task.py`** – Demonstra como adicionar tarefas usando `helper_functions.py`.  
- **`example_register.py`** – Mostra como registrar um novo usuário na API.  

Esses scripts ajudam a automatizar e integrar a API Task Manager em outras aplicações.

#

## Configuração ⚙️

Para rodar o projeto localmente:

```bash
# Clone o repositório
git clone https://github.com/rafaelmeller/django-task-manager.git

# Navegue até o diretório do projeto
cd django-task-manager

# Crie um ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Instale as dependências
pip install -r requirements.txt

# Aplique as migrações do banco de dados
python manage.py migrate

# (Opcional) Crie um superusuário para acessar o painel de administração do Django
python manage.py createsuperuser

# Inicie o servidor de desenvolvimento
python manage.py runserver
```

## Autor 👨🏻‍💻

Este projeto foi desenvolvido por **Rafael Meller**.

[![Linkedin Badge](https://img.shields.io/badge/-Rafael_Meller-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/rafaelmeller/)](https://www.linkedin.com/in/rafaelmeller/) 
[![Gmail Badge](https://img.shields.io/badge/-rafaelmeller.dev@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=rafaelmeller.dev@gmail.com)](mailto:rafaelmeller.dev@gmail.com)
#
## Licença 📝

Este projeto está licenciado sob a licença [MIT](./LICENSE).