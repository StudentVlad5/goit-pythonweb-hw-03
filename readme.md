# Web Message Storage Application

This is a Python-based web application developed as part of a FullStack Web Development assignment. It features a custom-built HTTP server that handles routing, static file serving, form processing, and data persistence using JSON and Jinja2 templates.

## Features

- Custom Routing: Handles / (Home), /message (Contact Form), and /read (Message History).

- Static Assets: Serves style.css and logo.png directly from the root directory.

- Form Processing: Captures user data via POST requests and stores it in a structured JSON format.

- Jinja2 Templating: Dynamically renders the /read page using the Jinja2 engine to display stored messages.

- Data Persistence: Saves all messages to storage/data.json with unique timestamps.

- Dockerized: Includes a Dockerfile for containerization and supports persistent storage via Docker Volumes.

## Tech Stack

- Python 3.11

- Jinja2 (Templating Engine)

- Docker (Containerization)

- HTTP Server (Python standard library)

## Project Structure

Plaintext

```
.
├── main.py         # Main server logic and routing
├── index.html      # Homepage
├── message.html    # Contact form page
├── read.html       # Jinja2 template for viewing messages
├── error.html      # 404 Error page
├── style.css       # Global styles
├── logo.png        # Application logo
├── Dockerfile      # Docker configuration
└── storage/
└── data.json       # Persistent JSON data storage
```

## Installation & Setup

Running Locally
Install dependencies:

```
pip install jinja2
```

Start the server:

```
python main.py
```

Access the app: Open http://localhost:3000 in your browser.

Running with Docker (Persistent Volumes)
To ensure your data survives container restarts, mount the storage folder using a volume.

1. Build the image:

```
docker build -t my-web-app .
```

2. Run the container:

For Windows (Git Bash):

```
MSYS_NO_PATHCONV=1 docker run -p 3000:3000 -v "$(pwd)/storage:/app/storage" my-web-app

```

For PowerShell:

PowerShell

```
docker run -p 3000:3000 -v "${PWD}/storage:/app/storage" my-web-app
```

## Data Format

Messages are stored in storage/data.json using the following schema:

JSON
{
"2026-03-14 17:14:28.045518": {
"username": "Vlad",
"message": "lets go\r\n"
},
"2026-03-14 17:14:54.537765": {
"username": "victoria",
"message": "i want to stay at home"
},
"2026-03-14 17:18:40.002594": {
"username": "Vlad",
"message": "Why?"
},
"2026-03-14 17:19:05.504368": {
"username": "Victoria",
"message": "i'm 😴 tired"
}
}

## Assignment Requirements Checklist

- [x] HTML pages for index.html and message.html.

- [x] Handling of static resources (style.css, logo.png).

- [x] Custom 404 error page (error.html).

- [x] Form data conversion to JSON with timestamps.

- [x] /read route using Jinja2 to display all messages.

- [x] Dockerfile implementation with Volumes support.
