# Project Thunderbird

## Project Overview

This project is a Python-based web application built with the Flask framework. The application is containerized using Docker. The application provides an email-based authentication system. Once authenticated, a user can view a master password for 1Password and unlock a media folder by providing an encrypted key.

The main features are:

*   **Email Authentication:** Users are authenticated by clicking a verification link sent to their email address. The link contains a unique token.
*   **Encrypted Key:** Along with the verification link, the user also receives an encrypted key.
*   **Master Password:** Once authenticated, the user can view a master password for 1Password.
*   **Media Unlock:** The user can use the encrypted key to unlock and view a list of media files.

The entry point of the application is `app/main.py`.

## Building and Running

This project is designed to be run using Docker.

1.  **Build and run the application:**
    ```bash
    ./setup.sh
    ```
    The application will be accessible at [http://localhost:5001](http://localhost:5001).

## Development Conventions

The project follows a standard Flask application structure, with the application logic contained within the `app` directory.

*   **Templates:** HTML templates are located in the `app/templates` directory.
*   **Static Assets:** Static assets (e.g., CSS, JavaScript) are located in the `app/static` directory.
*   **Configuration:** The authorized email addresses are stored in `config/authorized_emails.json`.
*   **Encryption Key:** The encryption key is stored in `secret.key`.

## Testing

To test the application flow, you can use `curl`.

1.  **Submit the login form:**
    ```bash
    curl -c cookies.txt -X POST -F 'email=<your_email>' http://localhost:5001/auth
    ```

2.  **Get the verification link and encrypted key:**

    Check the Docker logs for the verification link and the encrypted key:
    ```bash
    docker-compose logs
    ```

3.  **Click the verification link:**
    ```bash
    curl -L -b cookies.txt <verification_link>
    ```

4.  **Unlock the media folder:**
    ```bash
    curl -L -b cookies.txt -X POST -F 'key=<encrypted_key>' http://localhost:5001/unlock
    ```
