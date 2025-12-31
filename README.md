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
User Browser
↓
localhost:8080
↓
Docker Compose
↓
Container:5000
↓
Flask Application


The `/` endpoint returns the port the application believes it is running on.

---

## Docker Compose Mapping

```yaml
ports:
  - "8080:5000"


Left side → Host

Right side → Container

CI Pipeline Explanation

Checkout source code

Login to Docker Hub

Build Docker image

Tag image as dockerhub-username/containerized-flask-app:latest

Push image to Docker Hub

Run container

Verify /health endpoint

Design Decisions

Flask over FastAPI

Simpler and sufficient for demonstrating containers

Slim base image

Smaller image size and faster CI builds

Non-root user

Improves container security

Improvements With More Time

Add Docker HEALTHCHECK

Add unit tests

Use versioned image tags

Add Kubernetes manifests

Architecture Diagram
flowchart LR
    User -->|8080| Host
    Host -->|Port Mapping| DockerCompose
    DockerCompose -->|5000| Container
    Container --> FlaskApp

How to Run Locally
docker compose up --build


Access:

http://localhost:8080/

http://localhost:8080/health


---

# ✅ Final Verification Commands

```bash
docker compose up --build
curl http://localhost:8080/
curl http://localhost:8080/health