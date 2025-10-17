# Infinity Blog

A full-featured Flask blog application with user authentication, admin controls, and commenting system.

## Features

- **User Authentication**: Register, login, and logout functionality
- **Admin Controls**: Only admin users can create, edit, and delete posts
- **Commenting System**: Authenticated users can comment on blog posts with Gravatar support
- **Rich Text Editor**: CKEditor integration for creating and editing posts
- **Responsive Design**: Bootstrap-powered responsive UI
- **SQLite Database**: Lightweight database for storing users, posts, and comments
- **Environment Configuration**: Secure configuration with environment variables
- **Automated Setup**: Easy project initialization with setup script

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

3. Set up environment variables (recommended):
```bash
# Option 1: Use the setup script (recommended)
python setup.py

# Option 2: Manual setup
copy .env.example .env
# Then edit .env file with your preferred settings
```

4. Run the application:
```bash
python main.py
```

5. Open your browser and navigate to:
```
http://127.0.0.1:5001
```

### First Run
- If no users exist, an admin user will be created automatically
- Default admin credentials: admin@blog.com / admin123 (change these in .env file)
- The first registered user (ID: 1) will have admin privileges

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
├── setup.py             # Automated setup script
├── requirements.txt     # Python dependencies
├── .env.example         # Environment variables template
├── .gitignore          # Git ignore file
├── posts.db            # SQLite database (created automatically)
├── templates/          # HTML templates
├── static/            # CSS, JS, and image assets
├── FIXES_APPLIED.md    # Documentation of fixes applied
└── README.md          # This file
```

## Technologies Used

- **Flask 3.0.3** - Web framework
- **SQLAlchemy 2.0.44** - Database ORM
- **Flask-Login** - User session management
- **Flask-WTF** - Form handling and validation
- **Flask-CKEditor** - Rich text editor
- **Bootstrap 5** - Frontend framework
- **python-dotenv** - Environment variable management
- **SQLite** - Database
- **Custom Gravatar Integration** - User profile images

## Database Schema

- **Users**: Store user accounts with authentication
- **BlogPosts**: Store blog content with author relationships
- **Comments**: Store user comments linked to posts and authors

## Security Features

- Password hashing with PBKDF2-SHA256
- CSRF protection on all forms
- Admin-only decorators for sensitive operations
- User session management
- Environment variable support for sensitive configuration
- Proper authentication checks for admin functions

## Development

The application runs in debug mode by default. For production deployment:

1. Set `debug=False` in `main.py`
2. Use a production WSGI server like Gunicorn
3. Configure environment variables for sensitive data (see `.env.example`)
4. Use a production database like PostgreSQL
5. Generate a secure SECRET_KEY (setup.py does this automatically)

## Environment Variables

The application supports the following environment variables (see `.env.example`):

- `SECRET_KEY` - Flask secret key for sessions and CSRF protection
- `DATABASE_URL` - Database connection string
- `ADMIN_EMAIL` - Default admin user email (used only on first run)
- `ADMIN_PASSWORD` - Default admin user password (used only on first run)
- `ADMIN_NAME` - Default admin user name (used only on first run)
- `FLASK_ENV` - Flask environment (development/production)

## Troubleshooting

### Common Issues

**Import Errors**: Make sure all dependencies are installed:
```bash
python -m pip install -r requirements.txt
```

**Database Errors**: If you encounter database issues, delete `posts.db` and restart the application to recreate it.

**Template Errors**: Ensure you've run the setup script or manually configured environment variables.

**Admin Access**: The first registered user automatically becomes admin. If you need to reset admin access, delete the database and restart.

### Recent Fixes Applied

This project has been updated to fix several issues:
- ✅ Gravatar integration (custom implementation)
- ✅ Security improvements (environment variables)
- ✅ Database configuration fixes
- ✅ Admin access improvements
- ✅ Authentication error handling

See `FIXES_APPLIED.md` for detailed information about all fixes.

## License

This project is for educational purposes.
