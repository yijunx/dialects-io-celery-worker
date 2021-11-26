# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from app.app_config import conf


def send_email_verification(token: str, user_email: str, user_name: str):
    message = Mail(
        from_email="dialects.io@gmail.com",
        to_emails=user_email,
        subject="email verification",
        html_content=f"""

        <p>Dear {user_name.title()}</p>
        <br>
        <p>Please click below link to verify your email:</p>
        <br>
        <p>https://{conf.DOMAIN_NAME}/email_verification?token={token}</p>
        
        """,
    )
    try:
        sg = SendGridAPIClient(conf.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        # raise custom error here saying error handing email
        # server issue...
        raise e


def send_password_reset(token: str, user_name: str, user_email: str, login_method: str):
    """
    sending email for password reset"""

    content = f"""

        <p>Dear {user_name.title()}</p>
        <br>
        <p>Please click below link to reset your password:</p>
        <br>
        <p>https://{conf.DOMAIN_NAME}/reset_password?token={token}</p>
        
        """
    if login_method != "password":
        content = f"""

        <p>Dear {user_name.title()}</p>
        <br>
        <p>You dont login with password bro, use google or something<p>
        
        """
    message = Mail(
        from_email="dialects.io@gmail.com",
        to_emails=user_email,
        subject="password reset email",
        html_content=content,
    )
    try:
        sg = SendGridAPIClient(conf.SENDGRID_API_KEY)
        response = sg.send(message)
        print(response.status_code)
        # print(response.body)
        # print(response.headers)
    except Exception as e:
        # raise custom error here saying error handing email
        # server issue...
        raise e


if __name__ == "__main__":
    send_email_verification(
        token="token", user_email="user@email.com", user_name="user_name"
    )
