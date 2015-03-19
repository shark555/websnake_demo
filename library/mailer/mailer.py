import smtplib
from email.mime.text import MIMEText


class Mailer:
    def __init__(self):
        self._subject = ""
        self._from = 'root@localhost'
        self._to = ""
        self._message = ""
   
    def set_recipient_address(self, recipient_address):
        self._to = recipient_address

    def set_subject(self, subject):
        self._subject = subject

    def set_message(self, message):
        self._message = message

    def send(self):
        message = MIMEText(self._message)
        message['Subject'] = self._subject
        message['From'] = self._from
        message['To'] = self._to
        s = smtplib.SMTP('localhost')
        s.send_message(message)
        s.quit()       

