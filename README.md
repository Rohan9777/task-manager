# Task Manager API

A small REST API for managing tasks, built with Django and Django REST Framework as a Python intern assignment. It lets you create, list, view, update and delete tasks, and stores them in a local SQLite database.

## Tech stack

- Python 3.12 or newer
- Django 6.1
- Django REST Framework 3.18
- SQLite (no setup needed; the database file is created for you)

## Getting started

### 1. Clone the repository

```bash
git clone https://github.com/Rohan9777/task-manager.git
cd task-manager
```

### 2. Create and activate a virtual environment

Linux / macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
```

### 4. Create the database

The database file is not included in the repository, so run the migrations to create it:

```bash
python manage.py migrate
```

### 5. Start the server

```bash
python manage.py runserver
```

The API is now available at `http://127.0.0.1:8000/api/tasks/`. Opening that address in a browser shows Django REST Framework's browsable API, where you can try every endpoint without extra tools.

## API endpoints

| Method | URL | What it does |
| --- | --- | --- |
| GET | `/api/tasks/` | List all tasks |
| POST | `/api/tasks/` | Create a task |
| GET | `/api/tasks/<id>/` | Get one task |
| PUT | `/api/tasks/<id>/` | Update a task |
| DELETE | `/api/tasks/<id>/` | Delete a task |

URLs must end with a trailing slash.

### Task fields

| Field | Type | Notes |
| --- | --- | --- |
| `id` | integer | Set automatically |
| `title` | string | Required, up to 200 characters |
| `description` | string | Optional |
| `status` | string | `Pending` (default), `In Progress` or `Completed` |
| `created_at` | datetime | Set automatically |
| `updated_at` | datetime | Set automatically |

### Sample requests and responses

The examples use `curl`. Timestamps are in UTC.

#### Create a task

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Write the README", "description": "Explain the setup", "status": "Pending"}'
```

Response (`201 Created`):

```json
{
  "id": 1,
  "title": "Write the README",
  "description": "Explain the setup",
  "status": "Pending",
  "created_at": "2026-10-05T20:05:03.155725Z",
  "updated_at": "2026-10-05T20:05:03.155737Z"
}
```

Only `title` is required. If you leave out the others, `description` is empty and `status` is `Pending`.

#### List all tasks

```bash
curl http://127.0.0.1:8000/api/tasks/
```

Response (`200 OK`):

```json
[
  {
    "id": 1,
    "title": "Write the README",
    "description": "Explain the setup",
    "status": "Pending",
    "created_at": "2026-10-05T20:05:03.155725Z",
    "updated_at": "2026-10-05T20:05:03.155737Z"
  },
  {
    "id": 2,
    "title": "Push to GitHub",
    "description": "",
    "status": "Pending",
    "created_at": "2026-10-05T20:05:03.156930Z",
    "updated_at": "2026-10-05T20:05:03.156942Z"
  }
]
```

#### Get one task

```bash
curl http://127.0.0.1:8000/api/tasks/1/
```

Response (`200 OK`):

```json
{
  "id": 1,
  "title": "Write the README",
  "description": "Explain the setup",
  "status": "Pending",
  "created_at": "2026-10-05T20:05:03.155725Z",
  "updated_at": "2026-10-05T20:05:03.155737Z"
}
```

#### Update a task

`title` must be sent on every `PUT`. Fields you leave out keep their current value.

```bash
curl -X PUT http://127.0.0.1:8000/api/tasks/1/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Write the README", "status": "Completed"}'
```

Response (`200 OK`):

```json
{
  "id": 1,
  "title": "Write the README",
  "description": "Explain the setup",
  "status": "Completed",
  "created_at": "2026-10-05T20:05:03.155725Z",
  "updated_at": "2026-10-05T20:05:03.159418Z"
}
```

#### Delete a task

```bash
curl -X DELETE http://127.0.0.1:8000/api/tasks/1/
```

Response (`200 OK`):

```json
{
  "message": "Task deleted successfully"
}
```

### Error responses

#### Invalid data (`400 Bad Request`)

The response names each field that failed and why. A request without a `title`:

```bash
curl -X POST http://127.0.0.1:8000/api/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"description": "No title here"}'
```

```json
{
  "title": [
    "This field is required."
  ]
}
```

A request with a `status` that is not one of the three allowed values:

```json
{
  "status": [
    "\"Done\" is not a valid choice."
  ]
}
```

#### Task not found (`404 Not Found`)

```bash
curl http://127.0.0.1:8000/api/tasks/999/
```

```json
{
  "errors": "Task not found"
}
```

`GET` and `PUT` return the message under the key `errors`; `DELETE` returns it under `error`.

## Project structure

```
task-manager/
├── config/            # Project settings and root URL configuration
├── tasks/             # The tasks app
│   ├── models.py      # Task model
│   ├── serializers.py # Converts tasks to and from JSON
│   ├── views.py       # API views
│   ├── urls.py        # Task routes
│   └── migrations/    # Database migrations
├── manage.py
└── requirements.txt
```

## Notes

The project is configured for local development (`DEBUG = True` and a development secret key in `config/settings.py`). Change those settings before deploying it anywhere public.
