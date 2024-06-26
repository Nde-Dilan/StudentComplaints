import smtplib
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import MySQLdb

from PyQt5.uic import loadUiType

ui, _ = loadUiType("UI/complaint-request.ui")


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)

        self.quit1.clicked.connect(self.quitfunction)
        self.sendEmail.clicked.connect(self.sendfunction)
        self.show_courses()

    def sendfunction(self):
        import smtplib
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from email.mime.application import MIMEApplication
        #
        try:
            # Email configuration
            sender_email = self.sender_email.text()
            sender_password = self.sender_password.text()
            recipient_email = "heudan@gmail.com"
            subject = f"Student Complaint for {self.courseCombo.currentText()}"
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
            QMessageBox.information(self, "Info", "Email sent successfully!", QMessageBox.Ok)
        except smtplib.SMTPException as e:
          print(e)

    def quitfunction(self):
        self.close()

    def show_courses(self):
        self.db = MySQLdb.connect(host='localhost', user='root', password='123456789', db='complaints')
        self.cursor = self.db.cursor()

        self.cursor.execute('''
           SELECT CourseName FROM course
           ''')

        data = self.cursor.fetchall()
        for course in data:
            self.courseCombo.addItem(course[0])




def main():
    app = QApplication(sys.argv)

    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
