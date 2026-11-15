# Django Blog

A blog application built with Django. Posts are organized into categories (Sports, Politics, Business), each post has an author and a publishing status, and everything is managed through the Django admin panel.

## Features

- Category-based organization of blog posts
- Blog posts with title, auto-generated slug, category, author and status (draft/published)
- Featured post flag (`is_featured`) to highlight selected posts
- Author linked to Django's built-in `User` model
- Django admin with prepopulated slugs and search for quick content management

## Tech Stack

- Python 3
- Django
- SQLite (default Django database)

## Project Structure

```
Django-blog/
├── blog_main/        # Project settings, main URLs, WSGI/ASGI config
├── blog/             # Blog app: models, admin, views, templates
├── manage.py
└── README.md
```

## Data Models

**Category**

| Field           | Description                    |
|-----------------|--------------------------------|
| `category_name` | Name of the category           |
| `created_at`    | Set when the category is created |
| `updated_at`    | Updated on every save          |

**Blog**

| Field         | Description                              |
|---------------|------------------------------------------|
| `title`       | Post title                               |
| `slug`        | URL-friendly identifier                  |
| `category`    | Foreign key to `Category`                |
| `author`      | Foreign key to Django `User`             |
| `status`      | Draft or Published                       |
| `is_featured` | Marks the post as featured               |

## Getting Started

### Prerequisites

- Python 3.10 or newer
- pip

### Installation

1. Clone the repository

   ```bash
   git clone https://github.com/zaid78415-a11y/Django-blog.git
   cd Django-blog
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install django
   ```

4. Apply migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser to access the admin panel

   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server

   ```bash
   python manage.py runserver
   ```

   Open http://127.0.0.1:8000/ in your browser.

## Usage

1. Go to http://127.0.0.1:8000/admin/ and log in with your superuser account.
2. Add categories (for example Sports, Politics, Business).
3. Add blog posts, choosing a category and setting the status to Published. The slug fills in automatically from the title.
4. Mark posts as featured to highlight them.

## Future Improvements

- User registration and login
- Comments on posts
- Search and pagination
- Deployment (for example on AWS)

## Author

**Zaid Khan**
B.Sc. Computer Science graduate, Pune, India

## License

This project is for learning and portfolio purposes.
