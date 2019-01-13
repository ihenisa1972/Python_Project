import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Create Secure Connection Class
class EmailObject:

    # Initializer
    def __init__(self, password):
        self.password = password
        self.sender_email = "ihenisa1972@gmail.com"
        self.receiver_email = "ihenisapython@gmail.com"
        self.message = ""

    # Secure Connection Plain Text
    def CreateConnectionPlain(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.message)

    # Secure Connection HTML
    def CreateConnectionHTML(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.message.as_string())

    # Secure Connection Attachment
    def CreateConnectionAttachment(self):
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, self.receiver_email, self.text)

    # Simple Email
    def CreateEmailText(self):
        self.message = """\
        Subject: Hi there

        This message is sent from Python."""

     # Plain-text and HTML version
    def PlainTextAndHTMLVersion(self):
        self.message = MIMEMultipart("alternative")
        self.message["Subject"] = "multipart test"
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email

        # Create the plain-text and HTML version of your message
        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""
        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="http://www.realpython.com">Real Python</a> 
               has many great tutorials.
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        self.message.attach(part1)
        self.message.attach(part2)


    # Email with Attachment
    def EmailAttachment(self):
        # Create a multipart message and set headers
        self.subject = "An email with attachment from Python"
        self.body = "This is an email with attachment sent from Python"
        self.message = MIMEMultipart()
        self.message["From"] = self.sender_email
        self.message["To"] = self.receiver_email
        self.message["Subject"] = subject
        selfmessage["Bcc"] = receiver_email  # Recommended for mass emails

        # Add body to email
        self.message.attach(MIMEText(body, "plain"))

        filename = "document.txt"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            # Email client can usually download this automatically as attachment
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )

        # Add attachment to message and convert message to string
        self.message.attach(part)
        self.text = self.message.as_string()


if __name__ == "__main__":
    password = input("Type your password and press enter: ")

    Email1 = EmailObject(password)
    Email1.CreateEmailText()
    Email1.CreateConnectionPlain()
    Email1.PlainTextAndHTMLVersion()
    Email1.CreateConnectionHTML()
    Email1.EmailAttachment()
    Email1.CreateConnectionAttachment()

