import gspread
from google.oauth2.service_account import Credentials
import os
import json

class GoogleSheetsAuthError(Exception):
    """Custom exception for Google Sheets authentication errors."""
    pass

class GoogleSheetsAuth:
    def __init__(self, creds_json=None):
        """Initialize the Google Sheets authentication class.

        Args:
            creds_json (str, optional): JSON string containing Google credentials. Defaults to None.
        """
        self.creds_json = creds_json or os.environ.get('GOOGLE_APPLICATION_CREDENTIALS_JSON')
        self.client = self.authenticate()

    def authenticate(self):
        """Authenticate with Google Sheets API and create a client.

        Returns:
            gspread.Client: Authenticated Google Sheets client.

        Raises:
            GoogleSheetsAuthError: If credentials are not provided or authentication fails.
        """
        if self.creds_json:
            try:
                creds_info = json.loads(self.creds_json)
                creds = Credentials.from_service_account_info(creds_info,
                                                              scopes=['https://www.googleapis.com/auth/spreadsheets'])
                return gspread.authorize(creds)
            except Exception as e:
                raise GoogleSheetsAuthError(f"Authentication failed: {e}")
        else:
            raise GoogleSheetsAuthError("Google Sheets credentials not provided")

    def get_client(self):
        """Get the authenticated Google Sheets client.

         Returns:
             gspread.Client: Authenticated Google Sheets client.
         """
        return self.client