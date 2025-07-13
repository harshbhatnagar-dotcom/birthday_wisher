import os
import io
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

# Load service account from GitHub Secret
service_account_info = json.loads(os.environ["GDRIVE_KEY"])

credentials = service_account.Credentials.from_service_account_info(
    service_account_info,
    scopes=["https://www.googleapis.com/auth/drive.readonly"]
)

drive_service = build("drive", "v3", credentials=credentials)

# Replace with your real file ID from Google Drive
FILE_ID = "100377833253381618051"

request = drive_service.files().get_media(fileId=FILE_ID)
fh = io.FileIO("data.xlsx", "wb")
downloader = MediaIoBaseDownload(fh, request)

done = False
while not done:
    status, done = downloader.next_chunk()
    print(f"⬇️ Downloaded {int(status.progress() * 100)}% of data.xlsx")

