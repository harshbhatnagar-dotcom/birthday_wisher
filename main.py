import pandas as pd
import datetime
import smtplib
import os


# Load environment variables from .env
GMAIL = os.getenv("GMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def send_email(to, subject, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(GMAIL, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            s.sendmail(GMAIL, to, email_message)
            print(f"✅ Sent to: {to}")
    except Exception as e:
        print(f"❌ Failed to send to {to}. Reason: {e}")


df=pd.read_excel("data.xlsx")



today=datetime.datetime.now().strftime("%d/%m")

for index,item in df.iterrows():

    bday=item["Date"].strftime("%d/%m")
    

    if(today==bday):
        send_email(item["gmail"],"Happy Birthday",item["Message"])
