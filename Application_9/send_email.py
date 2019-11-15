from email.mime.text import MIMEText
import smtplib

def send_email(email,height, avg_height, count):
    from_email = "hitensidapara195@gmail.com"
    from_password = "8182@hiten@3682"
    to_email = email

    subject = "Height Data"
    message = f"Hey there, your height is <strong>{height}</strong>. <br> Average height of all is <strong>{avg_height}</strong> and that is calculated out <strong>{count}</strong> of people <br> Thanks!"

    msg = MIMEText(message, 'html')
    msg["Subject"] = subject
    msg["To"] = to_email
    msg["From"] = from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)