# Architecture Overview

This document describes the high-level architecture of the Containerized Flask App and how to render the diagrams included in this repository.

**Components**
- **Host**: Developer machine or CI runner that invokes Docker / Compose.
- **Docker Compose**: `docker-compose.yml` defines a single service `web` that builds from the repository root and names the container `flask_app`.
- **Dockerfile**: Builds an image from `python:3.11-slim`, installs `app/requirements.txt`, copies `app/` into `/app`, switches to non-root `appuser`, exposes port `5000`, and runs `main.py`.
- **Container**: Runs the Flask app which listens on port `5000` (environment variable `PORT`).
- **App code**: `app/main.py` exposes endpoints `/` and `/health`.
- **CI**: GitHub Actions workflow builds and pushes the image; it also runs the container for verification.

**Important port note (inconsistency)**
- `docker-compose.yml` maps host `8090` -> container `5000` (the file shows `"8090:5000"`).
- The repository `README.md` mentions `8080 -> 5000`.
- The CI workflow runs `docker run -d -p 8080:5000 ...`.

Please confirm which host port you want to use (8080 vs 8090). The diagrams include a short note about this mismatch.

**Files added**
- `docs/architecture.dot` — Graphviz DOT file for a directed diagram.
- `docs/architecture.puml` — PlantUML component diagram.

**How to render the diagrams locally**

Graphviz (DOT -> PNG):

```
REM Windows (cmd.exe) - requires Graphviz installed and `dot` available on PATH
dot -Tpng docs\architecture.dot -o docs\architecture.png
```

PlantUML (requires Java and plantuml.jar):

```
REM Example using plantuml.jar
java -jar plantuml.jar docs\architecture.puml
```

Alternatively, use online PlantUML viewers or VS Code PlantUML extension to view `docs/architecture.puml`.

**How to run the app locally with Docker Compose**

```
REM Build and run (Windows cmd)
docker compose up --build

REM The compose file maps host port 8090 -> container 5000 according to current file
REM So open http://localhost:8090/health
```

If you want to map host port 8080 instead, edit `docker-compose.yml` to change `8090:5000` to `8080:5000`.
