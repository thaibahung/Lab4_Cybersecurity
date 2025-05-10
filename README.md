# Vuln-App
A minimal Flask-based web application deliberately containing common security vulnerabilities for educational lab use. Containerized with Docker for consistent building and testing.

## Features:
- Flask backend with SQLite database
- Vulnerabilities included:
  - SQL Injection on the /search endpoint
  - Reflected XSS when echoing back the search parameter
  - Local File Inclusion on the /show endpoint
- Basic raw HTML frontend (no JavaScript frameworks)

## Getting started
### Prerequisites:
- [Docker](https://www.docker.com/) installed locally
### Build the Docker Image
From the project root:
```bash
docker build -t vuln-app
```
### Run the Container
```bash
docker run --rm -p 5000:5000 vuln-app
```
The application will run at `http://localhost:5000`

## Usage Examplse:
### 1. Search Users (SQL Injection + XSS)
- Normal search:
  ```bash
  curl "http://localhost:5000/search?name=hung"
  ```
- Exploit SQL Injection (bypass filter):
  ```bash
  curl "http://localhost:5000/search?name=alice' OR '1'='1"
  ```
- Trigger reflected XSS: Visit in browser: `http://localhost:5000/search?name=<script>alert('XSS')</script>`

### 2. View Server Files (Local File Inclusion)
- Read a known file:
  ```bash
  curl "http://localhost:5000/show?file=app.py"
  ```
- Traversal attack:
  ```bash
  curl "http://localhost:5000/show?file=../Dockerfile"
  ```
## Security Mitigation Tips
- Prevent SQL Injection: Use parameterized queries like `cursor.execute("SELECT ... WHERE name = ?", (name,))`.
- Prevent XSS: Escape or sanitize all user inputs before rendering.
- Prevent LFI: Restrict file paths, validate and whitelist filenames, avoid direct file system access using unchecked user input.
