from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import timedelta
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email_basic(sender, receiver, email_subject):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = 'christellproject@gmail.com'  # Enter your address
    receiver_email = 'christeljamescellose@gmail.com'  # Enter receiver address
    password = 'madagaskar312project' # Enter your gmail password

    email_html = """<html>
    <body>
        <p>Hello!</p>
        <p>This is Email Test with Airflow!</p>
        <br>
    </body>
    </html>"""

    message = MIMEMultipart("multipart")

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(email_html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)
    message["Subject"] = email_subject
    message["From"] = sender_email

    for i, val in enumerate(receiver):
        message["To"] = val

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

def init_email():
    sender = "christell projects@gmail.com" # add the sender gmail address here
    recipients = ["christeljamescellose@gmail.com", "christelljamescellose@gmail.com"] # add your e-mail recipients here
    subject = "Test Airflow" # add the subject of the e-mail you'd like here
    send_email_basic(sender, recipients, subject)

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': '04-02-2021',
    'email': ['christellproject@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 0
}

dag = DAG('email_automation', 
    default_args=default_args,
    dagrun_timeout=timedelta(minutes=5),
    # schedule_interval = '0 13 * * 1', # if you want to set up an automation schedule you can do that here
    catchup=False
    )

t1 = PythonOperator(
    task_id='send_email',
    python_callable=init_email,
    dag=dag
)

