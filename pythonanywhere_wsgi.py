# PythonAnywhere WSGI configuration for the Pharmacy Management System.
# On PythonAnywhere this file replaces /var/www/<username>_pythonanywhere_com_wsgi.py
# Database credentials and the Flask secret key live in ~/.pharm_env (chmod 600),
# never in this file. See the "Free Deployment (PythonAnywhere)" section of README.md.
import os
import sys

project_home = '/home/USERNAME/PHARMACY-MANAGEMENT'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

env_path = os.path.expanduser('~/.pharm_env')
if os.path.exists(env_path):
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key, value)

from app import app as application
