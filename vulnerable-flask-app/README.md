# Vulnerable Flask Application

This project is a simple Flask web application that intentionally includes vulnerabilities for educational purposes. It demonstrates common security issues such as SQL Injection and File Inclusion.

## Project Structure

```
vulnerable-flask-app
├── app
│   ├── __init__.py
│   ├── views.py
│   ├── models.py
│   ├── utils.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── search.html
│       └── file_viewer.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── main.js
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── init_db.sql
├── run.py
└── README.md
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd vulnerable-flask-app
   ```

2. **Build and run the application using Docker:**
   ```
   docker-compose up --build
   ```

3. **Access the application:**
   Open your web browser and navigate to `http://localhost:5000`.

## Usage

- The application has a search feature that is vulnerable to SQL Injection. You can test this by entering malicious SQL queries in the search input.
- The file viewer feature allows users to include files from the server, which can lead to sensitive information disclosure. You can test this by manipulating the file parameter in the URL.

## Important Note

This application is designed for educational purposes only. Do not deploy it in a production environment. Always follow best practices for security when developing real applications.