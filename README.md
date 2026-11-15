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

The project includes `schema.sql`, which contains the database schema used by the application.

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
