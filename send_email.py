import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(smtp_server, port, sender_email, sender_password, receiver_email, subject, plain_text, html_text):

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    part1 = MIMEText(plain_text, 'plain')
    part2 = MIMEText(html_text, 'html')

    msg.attach(part1)
    msg.attach(part2)

    try:
      
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print(f"Email successfully sent to {receiver_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")
