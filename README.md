# Visitor Management System

![Visitor Management System](https://img.shields.io/badge/Visitor-Management-blue.svg)

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview
📋 **Visitor Management System** is a web application designed to manage and track visitors in a facility. It allows for the registration of visitors, tracking their sign-in and sign-out times, and generating reports based on visitor data.

## Features
✨ **Features** include:
- 📊 Dashboard displaying total visitors, active visitors, and total sign-outs.
- 🗂️ Visitor registration with custom fields.
- 📅 Visitor sign-in and sign-out tracking.
- 📈 Reporting and data export capabilities.
- 🛡️ User authentication and role-based access control.
- 🎨 Responsive design with Bootstrap.

## Technologies
🔧 **Built with**:
- Django
- PostgreSQL
- Bootstrap 5
- Font Awesome

## Installation
📦 **To get started** with the Visitor Management System, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/ajmalrasouli/VMS.git
    cd VMS
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure the database**:
    - Ensure PostgreSQL is installed and running.
    - Create a database for the project.
    - Update `DATABASES` settings in `settings.py` with your database credentials.

5. **Apply migrations**:
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server**:
    ```sh
    python manage.py runserver
    ```

## Usage
🚀 **Using the Visitor Management System**:

1. **Log in** to the admin panel at `http://127.0.0.1:8000/admin/`.
2. **Add visitors** via the admin panel or through the public interface.
3. **Track visitors** as they sign in and out.
4. **View reports** and export data from the dashboard.

## Contributing
🤝 **Contributions** are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them.
    ```sh
    git commit -m "Add some feature"
    ```
4. Push to the branch.
    ```sh
    git push origin feature/your-feature-name
    ```
5. Open a pull request.

## License
📝 **License**: This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

🔗 **Useful Links**:
- [Project Repository](https://github.com/ajmalrasouli/VMS)
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
