import os
from smtplib import SMTP
import dotenv

from_email = "aliyuahmmad60@gmail.com"


class NotificationManager:
    """This class is responsible for sending notifications with the deal flight details."""

    def notifier(self, msg, to_mail):
        with SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=os.getenv("email_username"), password=os.getenv("email_password"))
            connection.sendmail(
                from_addr=from_email,
                to_addrs=to_mail,
                msg=msg
            )

