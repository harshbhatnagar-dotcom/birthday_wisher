import os
import io
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from dotenv import load_dotenv

# Load service account credentials from environment
service_account_info = json.loads(os.environ["GDRIVE_KEY"])
credentials = service_account.Credentials.from_service_account_info(
    service_account_info, scopes=["https://www.googleapis.com/auth/drive.readonly"]
)

# Connect to Drive API
service = build("drive", "v3", credentials=credentials)

# Download the file
FILE_ID = "100377833253381618051"  # Replace with your file ID from Drive
request = service.files().get_media(fileId=FILE_ID)
fh = io.FileIO("data.xlsx", "wb")
downloader = MediaIoBaseDownload(fh, request)

done = False
while not done:
    status, done = downloader.next_chunk()
    print(f"⬇️ Downloaded {status.progress()*100:.0f}%")
