import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

# First less secured app should be allowed on your GMail.

host = "smtp.gmail.com"
port = 587
username = "email@gmail.com"
password = "password"
from_email = username
to_list = ["email@gmail.com"]



class MessageUser():    # Class which can be imported if needed
    user_details = []
    messages = []       # Without E-mail final representation of message with name, date and total
    email_messages = [] # With E-mail ...
    base_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!
Team CFE
"""
    # Standard function to add name, amount & email where email is optional
    def add_user(self, name, amount, email=None):
        # Formatting the name & amount
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        # detail is a dictionary
        detail = {
            "name": name,
            "amount": amount,
        }
        # today denotes the date 
        today = datetime.date.today()
        date_text = '{today.month}/{today.day}/{today.year}'.format(today=today)
        # using dictionary makes it easier to update/add
        detail['date'] = date_text
        if email is not None: # if email != None
            detail["email"] = email
        # Finally user_details is the list that appends a dictionary
        self.user_details.append(detail)
    # Getter
    def get_details(self):
        return self.user_details
    # Setter
    def make_messages(self):
        if len(self.user_details) > 0:  # Fail Safe
            # Fetch user 1 by 1
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                # base message is attached format to replace {} substitution
                message = self.base_message
                new_msg = message.format(
                    name=name,
                    date=date,
                    total=amount
                )
                # .get() allows it to be none. whereas detail["email"] would raise an exception
                user_email = detail.get("email")
                if user_email:
                    # user_data dictionary with email and message
                    user_data = {
                        "email": user_email,
                        "message": new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        # Only messages with e-mail can be sent to
        if len(self.email_messages) > 0:
            for detail in self.email_messages:
                user_email = detail['email']
                user_message = detail['message']
                try:
                    # smtplib is in-built in python so we use it this way
                    # for third-party we import particular API using from abc import xyz
                    # xyz.somefunc()
                    email_conn = smtplib.SMTP(host, port)
                    # Hello for initiating e-mail transaction with server. 
                    email_conn.ehlo()
                    # The connection is secured so start TLS
                    email_conn.starttls()
                    # attempt login
                    email_conn.login(username, password)
                    # MIMEMultipart is for adding text/html formatted message
                    the_msg = MIMEMultipart("alternative")
                    the_msg['Subject'] = "Billing Update!"
                    the_msg["From"] = from_email
                    the_msg["To"]  = user_email 
                    # plain or html
                    part_1 = MIMEText(user_message, 'plain')
                    the_msg.attach(part_1)
                    email_conn.sendmail(from_email, [user_email], the_msg.as_string())
                    email_conn.quit()
                except smtplib.SMTPException:
                    print("Error sending message")
            return True
        return False


obj = MessageUser()
obj.add_user("Justin", 123.32, email='email@gmail.com')
obj.add_user("jOhn", 94.23, email='email@gmail.com')
obj.add_user("Sean", 93.23, email='email@gmail.com')
obj.add_user("Emilee", 193.23, email='email@gmail.com')
obj.add_user("Marie", 13.23, email='email@gmail.com')
obj.get_details()

obj.send_email()