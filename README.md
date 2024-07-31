
# E-Learning Platform Backend

## Description

This is the backend for an e-learning platform developed using Django. It provides APIs for managing courses, posts, and comments, along with user authentication (signup and login).

## Setup Locally

### Prerequisites

- Python 3.8 or higher
- Django 3.2 or higher
- PostgreSQL (or another database of your choice)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/your-username/e-learning-platform-backend.git
    cd e-learning-platform-backend
    ```

2. **Create and activate a virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate 
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the database**

    Update your database configuration in `settings.py`.

    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

    Then apply the migrations:

    ```bash
    python manage.py migrate
    ```

5. **Run the development server**

    ```bash
    python manage.py runserver
    ```

    The server will be running at `http://127.0.0.1:8000/`.

## Hosted Version

The hosted version of the e-learning platform can be accessed at: [https://your-hosted-app.com](https://your-hosted-app.com)

## API Endpoints

Apart from signup and login, the following functionalities are provided:

### Comments

- **List comments for a post**

    ```http
    GET /posts/<int:post_id>/comments/
    ```

### Courses

- **List all courses**

    ```http
    GET /courses/
    ```

- **Get details of a specific course**

    ```http
    GET /courses/<int:id>/
    ```

### Posts

- **List all posts**

    ```http
    GET /posts/
    ```

- **Get details of a specific post**

    ```http
    GET /posts/<int:id>/
    ```

- **Create a new post**

    ```http
    POST /posts/new_post/
    ```

- **Create a new course**

    ```http
    POST /posts/new_course/
    ```

- **Create a new comment for a specific post**

    ```http
    POST /posts/<int:post_id>/new_comment/
    ```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.


