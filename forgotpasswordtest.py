import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_test_email():
    sender_email = "iamashwathy@gmail.com"
    receiver_email = "malarcomputer2023@gmail.com"
    password = "lort qfyo kece juuu"

    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Email"
    message["From"] = sender_email
    message["To"] = receiver_email

    text = "This is a test email sent from Python."
    html = """\
    <html>
      <body>
        <p>This is a test email sent from Python.<br>
           <b>It works!</b>
        </p>
      </body>
    </html>
    """

    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    message.attach(part1)
    message.attach(part2)

    try:
        print(f"Connecting to SMTP server for {sender_email}...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, password)
            server.sendmail(
                sender_email, receiver_email, message.as_string()
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    send_test_email()