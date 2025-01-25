# Module: data_storage.py

# Google Sheets Integration
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Firebase Integration
import firebase_admin
from firebase_admin import credentials, firestore

# Google Sheets Setup
def init_google_sheets(json_keyfile_path, sheet_name):
    """
    Initialize Google Sheets client.

    Args:
        json_keyfile_path (str): Path to the Google Sheets service account JSON key.
        sheet_name (str): Name of the Google Sheet to use.

    Returns:
        gspread.models.Sheet: The first sheet of the Google Sheet document.
    """
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds = ServiceAccountCredentials.from_json_keyfile_name(json_keyfile_path, scope)
    client = gspread.authorize(creds)
    sheet = client.open(sheet_name).sheet1
    return sheet

# Function to append data to Google Sheets
def append_to_google_sheets(sheet, comment, sentiment_score, sentiment_magnitude):
    """
    Append data to a Google Sheet.

    Args:
        sheet (gspread.models.Sheet): The Google Sheet to append to.
        comment (str): User comment.
        sentiment_score (float): Sentiment score of the comment.
        sentiment_magnitude (float): Sentiment magnitude of the comment.
    """
    sheet.append_row([comment, sentiment_score, sentiment_magnitude])

# Firebase Firestore Setup
def init_firestore(json_keyfile_path):
    """
    Initialize Firebase Firestore client.

    Args:
        json_keyfile_path (str): Path to the Firebase service account JSON key.

    Returns:
        firestore.Client: The Firestore client.
    """
    cred = credentials.Certificate(json_keyfile_path)
    if not firebase_admin._apps:
        firebase_admin.initialize_app(cred)
    return firestore.client()

# Function to store data in Firebase Firestore
def store_in_firestore(db, comment, sentiment_score, sentiment_magnitude):
    """
    Store data in Firebase Firestore.

    Args:
        db (firestore.Client): The Firestore client.
        comment (str): User comment.
        sentiment_score (float): Sentiment score of the comment.
        sentiment_magnitude (float): Sentiment magnitude of the comment.
    """
    doc_ref = db.collection("comments").document()
    doc_ref.set({
        "comment": comment,
        "sentiment_score": sentiment_score,
        "sentiment_magnitude": sentiment_magnitude
    })

# Example Usage
if __name__ == "__main__": # The code below will only run if this script is executed directly
                            # The if __name__ == "__main__": block is used to 
                            # prevent the code inside it from running when the script is 
                            # imported as a module
    # Google Sheets Example
    sheets_keyfile = "path_to_google_sheets_service_account.json"
    sheet_name = "Your Google Sheet Name"
    sheet = init_google_sheets(sheets_keyfile, sheet_name)
    append_to_google_sheets(sheet, "Service was great!", 0.9, 0.7)

    # Firebase Example
    firestore_keyfile = "path_to_firebase_service_account.json"
    db = init_firestore(firestore_keyfile)
    store_in_firestore(db, "Service was great!", 0.9, 0.7)
