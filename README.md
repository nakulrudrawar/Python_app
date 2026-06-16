# Python_app

A simple Flask application deployed via Jenkins CI/CD pipeline.

## Features
- Flask web application
- Automated deployment through Jenkins
- Runs on port 5000
- Accessible at 0.0.0.0:5000

## Requirements
- Python 3.x
- Flask 3.1.3
- Gunicorn 23.0.0

## Installation
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Running the Application
```bash
python3 app.py
```

## Deployment
The application is automatically deployed using the Jenkinsfile through CI/CD pipeline....