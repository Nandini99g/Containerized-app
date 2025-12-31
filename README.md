# Containerized Flask Application

## Overview
This project demonstrates a containerized Python Flask application using Docker, Docker Compose, and GitHub Actions CI.

---

## Application Endpoints

| Endpoint | Description |
|-------|------------|
| `/` | Returns app name and running port |
| `/health` | Health check endpoint |

---

## Port Explanation (Important)

- The Flask app listens on port **5000**, read from the `PORT` environment variable.
- The container exposes port **5000**.
- Docker Compose maps host port **8080** to container port **5000**.

### Traffic Flow
