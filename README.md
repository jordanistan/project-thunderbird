# Project Thunderbird

Hello! This project is a special application designed to help you with a specific task. You don't need to worry about the technical details. Just follow the simple steps below to get it running.

## How to Start the Application

To start the application, you just need to run a single script. This script will do everything for you.

**1. Open a Terminal**

*   **On macOS:** Open the "Terminal" application. You can find it in your "Applications" folder, inside the "Utilities" folder.
*   **On Windows:** Open the "PowerShell" application. You can find it by searching for "PowerShell" in the Start menu.

**2. Run the Setup Script**

Once you have the terminal open, you will need to navigate to this project's directory. Then, type the following command and press Enter:

```bash
./setup.sh
```

That's it! The script will take care of everything. It will start the application for you.

## How to Use the Application

Once the application is running, you can access it by opening your web browser and going to the following address:

[http://localhost:5001](http://localhost:5001)

**1. Log In**

*   You will be taken to a login page. Enter your email address and click "Log In".

**2. Verify Your Email**

*   After you log in, the application will send a verification link and an encrypted key to the terminal window where you ran the `setup.sh` script.
*   Find the line that says "Click this link to verify your email:" and copy the link.
*   Paste the link into your web browser.

**3. View the Master Password**

*   After you verify your email, you will be taken to a page that displays the master password for 1Password.

**4. Unlock the Media Folder**

*   On the same page, you will see a form to unlock the media folder.
*   Go back to the terminal window and find the line that says "Encrypted key:".
*   Copy the encrypted key.
*   Paste the key into the "Enter your encrypted key" field on the web page and click "Unlock".
*   You will then be able to see a list of all the media files.
