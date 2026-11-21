# Pharmacy Management System

A web-based Pharmacy Management System developed using Python Flask and MySQL to manage pharmacy-related operations through a simple and user-friendly interface.

## Overview

The Pharmacy Management System is designed to simplify pharmacy management by providing a web-based platform backed by a MySQL database.

The application uses Flask for backend development and MySQL for database management.

## Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Database:** MySQL
- **Database Connector:** MySQL Connector for Python

## Project Structure

```text
PHARMACY-MANAGEMENT/
│
├── static/
├── templates/
├── app.py
├── API_DESIGN.txt
├── schema.sql
├── test_id_logic.py
├── relational_schema_diagram.png
├── ref.png

```

## Prerequisites

Make sure you have installed:

- Python
- MySQL Server
- MySQL Workbench (optional)
- Git

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Malavika1105/PHARMACY-MANAGEMENT.git
```

### 2. Navigate to the Project Directory

```bash
cd PHARMACY-MANAGEMENT
```

### 3. Install Required Dependencies

```bash
python -m pip install flask mysql-connector-python
```

### 4. Configure the MySQL Database

- Start your MySQL server.
- Create the database required by the application.
- Import the database structure using the provided `schema.sql` file.
- Update the database connection credentials in `app.py` according to your local MySQL configuration.

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

Visit:

```text
http://127.0.0.1:5000
```

## Database

The project includes `schema.sql`, which contains the database schema used by the application (tables plus the `expiry_tracking` view used by the expiry page).

## Configuration (no secrets in code)

The app reads all settings from environment variables:

| Variable | Default | Purpose |
| --- | --- | --- |
| `DB_HOST` | `localhost` | MySQL host |
| `DB_PORT` | `3306` | MySQL port |
| `DB_USER` | `root` | MySQL user |
| `DB_PASSWORD` | _(empty)_ | MySQL password |
| `DB_NAME` | `LOGIN_1` | Database name |
| `SECRET_KEY` | _(random per start)_ | Flask session key; always set this in production |

## Free Deployment (PythonAnywhere)

The free tier of PythonAnywhere includes a MySQL database, so the app can run there with no paid plan:

1. Push this repository to GitHub.
2. Create a free account at pythonanywhere.com and open a Bash console.
3. `git clone <this repo URL>` and `pip install --user -r PHARMACY-MANAGEMENT/requirements.txt`.
4. On the Databases tab, set a MySQL password and create a database named `LOGIN_1` (PythonAnywhere names it `<username>$LOGIN_1`).
5. Open the MySQL console from the Databases tab and run the table and view definitions from `schema.sql` (skip the `CREATE DATABASE` and `USE` lines).
6. On the Web tab, add a new Flask web app pointing at the cloned project, then edit the WSGI file to set the environment variables above (`DB_HOST` is `<username>.mysql.pythonanywhere-services.com`, `DB_USER` and `DB_NAME` use the `<username>$LOGIN_1` form, plus `DB_PASSWORD` and `SECRET_KEY`) and import the Flask app as `application`.
7. Reload the web app. The site is live at `https://<username>.pythonanywhere.com`.

## Testing

The project includes a Python testing file:

```text
test_id_logic.py
```

## Author

**Malavika Sunooj**

B.Tech Computer Science and Engineering

## License

This project is intended for academic and educational purposes.
