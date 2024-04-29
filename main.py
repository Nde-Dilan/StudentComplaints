import smtplib
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


from PyQt5.uic import loadUiType

ui, _ = loadUiType("UI/complaint-request.ui")


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.quit1.clicked.connect(self.quitfunction)
        self.sendEmail.clicked.connect(self.sendfunction)
        # self.fill_book_db()

    def sendfunction(self):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        #TODO:
        try:
            # Email configuration
            sender_email = self.sender_email.text()
            sender_password = self.sender_password.text()
            recipient_email = "heudan@gmail.com"
            subject = "Student Complaint"
            body = self.contentEmail.toPlainText()

            # SMTP server settings (for Gmail)
            smtp_server = "smtp.gmail.com"
            smtp_port = 587

            # Create the MIME message
            msg = MIMEMultipart()
            msg["From"] = sender_email
            msg["To"] = recipient_email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain"))

        # Establish a secure connection and send the email

            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, recipient_email, msg.as_string())
        except smtplib.SMTPException as e:
          print(e)
        QMessageBox.information(self, "Info", "Email sent successfully!", QMessageBox.Ok)
    def quitfunction(self):
        self.close()




def main():
    app = QApplication(sys.argv)

    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
