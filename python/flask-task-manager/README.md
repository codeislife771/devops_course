# Flask Task Manager

A simple web application for managing tasks with a modern UI.

## Features

- Create, edit, and delete tasks
- Modern responsive design
- Real-time updates without page refresh
- Docker ready

## Quick Start

### Local Development

```bash
# Clone and setup
git clone <your-repo-url>
cd flask-task-manager

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/macOS

# Install and run
pip install -r requirements.txt
python app.py
```

Open: http://localhost:5000

### Docker

```bash
# Build and run
docker build -t flask-task-manager .
docker run -p 5000:5000 flask-task-manager
```

**With data persistence:**
```bash
# Option 1: File mount (development)
docker run -p 5000:5000 -v ${PWD}/tasks.json:/app/tasks.json flask-task-manager

# Option 2: Named volume (production)
docker volume create task-data
docker run -p 5000:5000 -v task-data:/app flask-task-manager
```

**Management commands:**
```bash
docker ps                    # View running containers
docker stop <container-id>   # Stop container
docker rm <container-id>     # Remove container
```

Open: http://localhost:5000

## Tech Stack

- **Backend**: Flask (Python 3.10+)
- **Frontend**: JavaScript, CSS
- **Storage**: JSON file
- **Container**: Docker

## Project Structure

```
├── app.py              # Flask application
├── requirements.txt    # Dependencies
├── Dockerfile         # Docker configuration
├── tasks.json         # Data storage
└── templates/
    └── index.html     # UI template
```
