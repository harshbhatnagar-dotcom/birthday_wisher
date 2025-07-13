import os
import io
import json
import pandas
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Load the service account key JSON from environment
service_account_info = json.loads(os.environ["GDRIVE_KEY"])

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=["https://www.googleapis.com/auth/drive.readonly"]
)

# Create Drive API client
drive_service = build("drive", "v3", credentials=credentials)

# ✅ Replace this with actual file ID from Google Drive share link
FILE_ID = "1HJRO-8fTCoGsrstH9STntabo6gAPnloC"

request = drive_service.files().get_media(fileId=FILE_ID)
fh = io.FileIO("data.xlsx", "wb")
downloader = MediaIoBaseDownload(fh, request)

done = False
while not done:
    status, done = downloader.next_chunk()
    print(f"⬇️ Downloaded {int(status.progress() * 100)}% of data.xlsx")
    df= pd.read_excel("data.xlsx")
    for index, item in df.iterrows():
        print(item["Date"])
