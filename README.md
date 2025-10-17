# Infinity Blog

A full-featured Flask blog application with user authentication, admin controls, and commenting system.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Admin Controls**: Only admin users can create, edit, and delete posts
- **Commenting System**: Authenticated users can comment on blog posts
- **Rich Text Editor**: CKEditor integration for creating and editing posts
- **Responsive Design**: Bootstrap-powered responsive UI
- **SQLite Database**: Lightweight database for storing users, posts, and comments

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd Py-Day69
```

2. Install the required packages:
```bash
python -m pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

4. Open your browser and navigate to:
```
http://127.0.0.1:5001
```

## Usage

### Admin Access
- The first registered user (ID: 1) automatically becomes the admin
- Admin users can:
  - Create new blog posts
  - Edit existing posts
  - Delete posts

### Regular Users
- Can register and login
- Can comment on blog posts
- Can view all published content

## Project Structure

```
Py-Day69/
├── main.py              # Main Flask application
├── forms.py             # WTForms for user input
├── requirements.txt     # Python dependencies
├── posts.db            # SQLite database (created automatically)
├── templates/          # HTML templates
├── static/            # CSS, JS, and image assets
└── README.md          # This file
```

## Technologies Used

- **Flask 3.0.3** - Web framework
- **SQLAlchemy 2.0.44** - Database ORM
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and validation
- **Flask-CKEditor** - Rich text editor
- **Bootstrap 5** - Frontend framework
- **SQLite** - Database

## Database Schema

- **Users**: Store user accounts with authentication
- **BlogPosts**: Store blog content with author relationships
- **Comments**: Store user comments linked to posts and authors

## Security Features

- Password hashing with PBKDF2-SHA256
- CSRF protection on all forms
- Admin-only decorators for sensitive operations
- User session management

## Development

The application runs in debug mode by default. For production deployment:

1. Set `debug=False` in `main.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables for sensitive data
4. Use a production database like PostgreSQL

## License

This project is for educational purposes.
