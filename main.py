import pandas as pd
import datetime
import smtplib
import os

# Load environment variables from GitHub Secrets
GMAIL = os.getenv("GMAIL")
GMAIL_PASSWORD = os.getenv("GMAIL_PASSWORD")

def send_email(to, subject, message):
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as s:
            s.starttls()
            s.login(GMAIL, GMAIL_PASSWORD)
            email_message = f"Subject: {subject}\n\n{message}"
            s.sendmail(GMAIL, to, email_message)
            print(f" Sent to: {to}")
    except Exception as e:
        print(f" Failed to send to {to}. Reason: {e}")

try:
    df = pd.read_excel("data.xlsx")
except Exception as e:
    print(f" Failed to read data.xlsx: {e}")
    exit()

today = datetime.datetime.now().strftime("%d/%m")

for _, item in df.iterrows():
    if pd.isnull(item.get("Date")) or pd.isnull(item.get("gmail")):
        continue

    try:
        bday = item["Date"].strftime("%d/%m")
        print(bday)
        if today == bday:
            message = item.get("Message", "Wishing you a wonderful birthday! ")
            send_email(item["gmail"], " Happy Birthday!", message)
    except Exception as e:
        print(f" Error processing row: {e}")
