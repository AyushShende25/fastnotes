#  FastNotes

FastNotes is a lightweight and asynchronous RESTful API for a simple note-taking application, built with **FastAPI**, **SQLAlchemy (async)**, and **PostgreSQL**.

---

##  Features

- Create, read, update, and delete notes
- Asynchronous SQLAlchemy database access
- Modular project structure
- Pydantic-based validation
- Alembic support for migrations

---

##  Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy (async)](https://docs.sqlalchemy.org/en/20/orm/extensions/asyncio.html)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) for migrations
- [PostgreSQL](https://www.postgresql.org/)
- [Pydantic](https://docs.pydantic.dev/) for data validation
- [Uv](https://docs.astral.sh/uv/) for project management

---

##  Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AyushShende25/fastnotes.git
   cd fastnotes
   ```

2. **Env Variables**
    create an .env file in the root directory and provide the needed env variables.
    ```sh
    # we only need one variable
    DATABASE_URL=your postgres db url here, remember to use async driver 
    ```

3. **Apply Migrations**
    ```bash
    uv run alembic upgrade head
    ```

4. **Run Server**
    run the development server with the following command explore the docs at (http://127.0.0.1:8000/docs). UV also installs the required dependencies when you run this command for the first time.
    ```bash
    uv run fastapi dev app/main.py
    ```

### With Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/AyushShende25/fastnotes.git
   cd fastnotes
   ```
2. **Run Containers**
    ```bash
    docker compose up
    ```
3. **Apply Migrations**
    ```bash
    docker compose exec api uv run alembic upgrade head
    ```