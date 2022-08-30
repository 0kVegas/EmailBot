"""
Functions File for sending emails
"""

# ----Imports----
from random import randrange
from email.message import EmailMessage
from datetime import datetime, date
import smtplib
import ssl


# ----Functions----
# ---Time---
def getDate():
    return date.today()  # Today's date (YYYY-MM-DD)


def getTime():
    now = datetime.now()
    time = now.strftime('%H %M %S')
    time = time.split(' ')  # [Hours, Minutes, Seconds]
    return time


def CheckTime(time):  # Get time parameters
    if 20 > int(time[0]) > 9:
        return True
    return False


def randTime():
    return randrange(3, 10)  # Random time to wait


def Pause():  # Pause before sending the next email
    temp = int(getTime()[1])
    temp += randTime()
    if temp > 60:
        temp -= 60
    return temp  # Time it's waiting for


# ---Text Files---
def OpenList(email):  # Get emails
    EmailList = open(email, 'r')
    text = EmailList.readline()
    EmailList.close()
    List = text.split(' ')
    return List  # List of all emails


def AddEmails(email):  # Add email to EmailTextFile.txt
    EmailList = open('EmailTextFile.txt', 'a')
    EmailList.write(email)
    EmailList.close()


def Receiver():  # Get email from email list
    return OpenList('EmailTextFile.txt')[0]  # Oldest email on the list


def AppendItem():  # Append email, time and date to SentTo.txt
    Emails = open('SentTo.txt', 'a')
    time = getTime()
    time = ':'.join(time)
    Date = str(getDate())
    text = [Receiver(), time, Date]
    text = ' '.join(text)
    Emails.write(text)
    Emails.write('\n')  # email@domainName.com Hour:Minute:Second YYYY-MM-DD
    Emails.close()


def PopItem(Emails):  # Deletes email from EmailTextFile.txt
    Emails.pop(0)
    Emails = ' '.join(Emails)
    EmailList = open('EmailTextFile.txt', 'w')
    EmailList.write(Emails)
    EmailList.close()
    return OpenList('EmailTextFile.txt')


def uploadEmails():  # Upload all emails in EmailsToAdd.txt to EmailTextFile.txt
    emails = OpenList('EmailsToAdd.txt')
    for i in range(len(emails)):
        AddEmails(emails[i])
        print(f"Uploaded: {emails[i]}")
    print('Finished uploads')


# ----Classes----
class Email:
    def __init__(self, emailReceiver):
        # Message
        self.subject = "Business Proposal"

        self.body = """
        Hi my name is Martin. I took interest in your small business, and I would like to do advertisements for you.
        Please contact me at (email here) if you're interested.
        """

        # Info
        self.emailSender = 'rosetico2001@gmail.com'
        self.emailPassword = 'gmlpudbmrmehyepe'
        self.emailReceiver = emailReceiver
        self.em = EmailMessage()

        # Format
        self.em['From'] = self.emailSender
        self.em['To'] = self.emailReceiver
        self.em['Subject'] = self.subject

        self.context = ssl.create_default_context()

    def send(self):  # Send email
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=self.context) as smtp:
            smtp.login(self.emailSender, self.emailPassword)
            smtp.sendmail(self.emailSender, self.emailReceiver, self.em.as_string())


if __name__ == '__main__':
    print(getDate())
