import requests
from core.settings import DEFAULT_FROM_EMAIL, EMAIL_SERVER_TOKEN
import logging


logger = logging.getLogger(__name__)


server_token = EMAIL_SERVER_TOKEN
template_id = ""

url = "https://api.postmarkapp.com/email"
headers = {"X-Postmark-Server-Token": server_token, "Content-Type": "application/json", "Accept":"application/json"}


def send_email(recipient_email, data,subject, html_body):
   
    body = {
        "From": DEFAULT_FROM_EMAIL,
        "To": recipient_email,
        "Subject": subject,
        "TemplateModel":data,
        "HtmlBody": html_body,
        "InlineCss": True,
    }
      
    response = requests.post(url, headers=headers, json=body).json()
   

    if response["Message"] == "OK" and response["ErrorCode"]==0:
        message = "Email sent successfully!"
        logging.info(msg=message)
   
    else:
        message = f'Error sending email: Message: {response["Message"]}, Error code: {response["ErrorCode"]}'
       
        logging.error(msg=message)
    

from authentication.emails.templates.reset_password import reset_password_template
def reset_email_password(recipient_email,employee_name, code):
    subject = 'Reset Password'
    data = {'employee_name':employee_name, 'code': code}
    html_body = reset_password_template.format(employee_name=employee_name, code=code)

    send_email(
        recipient_email= recipient_email,
        data=data,
        subject=subject,
        html_body=html_body,
    )


from authentication.emails.templates.register_user import register_user_template
def new_account_email(recipient_email, client_name):
    subject = 'New account created'
    data = {'client_name':client_name}
    html_body = register_user_template.format(client_name=client_name)

    send_email(
        recipient_email=recipient_email,
        data=data,
        subject=subject,
        html_body=html_body,
    )

from authentication.emails.templates.confirm_reset import confirm_reset_template
def confirm_reset_email(recipient_email, client_name):
    subject = 'Confirm password reset'
    data = {'client_name':client_name}
    html_body = confirm_reset_template.format(client_name=client_name)

    send_email(
        recipient_email=recipient_email,
        data=data,
        subject=subject,
        html_body=html_body,
    )