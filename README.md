# Keylogger

This project is a basic keylogger tool written in Python. It utilizes the `pynput` library to listen to and record keyboard events. The recorded keystrokes are saved to a log file, and the tool can detect both alphanumeric and special keys.

## Features

- **Key Logging:** Capture and record keystrokes.
- **Log File:** Save captured keystrokes to a text file.
- **Console Output:** Print detected key events to the console.

## Requirements

- Python 3.x
- Required Module: `pynput`

## Usage

1. **Install `pynput`:**
   - Ensure the `pynput` library is installed. You can install it via pip:
     ```bash
     pip install pynput
     ```

2. **Run the Script:**
   - Execute the Python script to start logging keystrokes.

3. **View Logs:**
   - Keystrokes will be saved to `log.txt` in the same directory as the script.
   - Alphanumeric and special key presses will be displayed in the console.

4. **Stop Logging:**
   - Press the `Esc` key to stop the keylogger.

## Note

- This script should be used responsibly and only for ethical purposes.
- Ensure you have permission to log keystrokes on the device
