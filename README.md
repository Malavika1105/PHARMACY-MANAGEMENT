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

## Free Deployment (TiDB Cloud + Render)

The app is deployed for free with TiDB Cloud Starter (free MySQL-compatible database) and Render (free web service). Neither requires a card. Live example: the maintainer's instance runs at a `*.onrender.com` URL.

### 1. Database: TiDB Cloud Starter

1. Sign up at tidbcloud.com and create a **Starter** cluster (free: 5 GiB storage + 50M RU/month; set the spending limit to $0).
2. On the cluster's Connect dialog, note the host, port `4000`, and username, and set/reset the password.
3. Create the database and load the schema (requires a MySQL client and TLS):

   ```bash
   mysql -h <HOST> -P 4000 -u <USER> -p --ssl-ca=/etc/ssl/certs/ca-certificates.crt -e "CREATE DATABASE IF NOT EXISTS LOGIN_1;"
   mysql -h <HOST> -P 4000 -u <USER> -p --ssl-ca=/etc/ssl/certs/ca-certificates.crt LOGIN_1 < schema.sql
   ```

### 2. Web app: Render

1. Push this repository to GitHub.
2. At dashboard.render.com, choose **New > Web Service** and connect the repo.
3. Settings: Runtime `Python 3`, Build Command `pip install -r requirements.txt`, Start Command `gunicorn app:app`, Instance Type **Free ($0/month)**.
4. Add these environment variables (Environment tab):
   - `DB_HOST` = the TiDB host, `DB_PORT` = `4000`, `DB_USER`, `DB_PASSWORD` = the TiDB credentials
   - `DB_NAME` = `LOGIN_1`
   - `DB_SSL_CA` = `/etc/ssl/certs/ca-certificates.crt`
   - `SECRET_KEY` = any long random string (`python3 -c "import secrets; print(secrets.token_hex(32))"`)
5. Click **Deploy web service**. Render gives you a public `https://<name>.onrender.com` URL (a suffix may be added if the name is taken).

After that, every `git push` to the connected branch redeploys automatically. The free web service sleeps after ~15 minutes without traffic; the first request after a sleep can take up to a minute.

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
