# Project Thunderbird

## Project Overview

This project is a Python-based web application built with the Flask framework. The application is containerized using Docker. Based on the project structure and dependencies, it is intended to have user authentication (`auth.py`), speech-to-text (`stt.py`), and text-to-speech (`tts.py`) capabilities, although these features are not yet implemented. The entry point of the application is `app/main.py`.

## Building and Running

This project is designed to be run using Docker.

1.  **Build the Docker image:**
    ```bash
    docker-compose build
    ```

2.  **Run the application:**
    ```bash
    docker-compose up
    ```
    The application will be accessible at [http://localhost:5001](http://localhost:5001).

## Development Conventions

The project follows a standard Flask application structure, with the application logic contained within the `app` directory.

*   **Templates:** HTML templates are located in the `app/templates` directory.
*   **Static Assets:** Static assets (e.g., CSS, JavaScript) are located in the `app/static` directory.

While the file structure suggests a separation of concerns (e.g., `auth.py`, `stt.py`, `tts.py`), the specific coding style and conventions are not yet established.
