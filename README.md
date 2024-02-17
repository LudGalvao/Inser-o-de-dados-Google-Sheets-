# PySheetsInsert

PySheetsInsert is a Python tool for inserting data into Google Sheets.

## Tools Used

- **google-auth**: Library for authentication with Google APIs.
- **google-auth-oauthlib**: Library for OAuth2 authentication flows with Google.
- **googleapiclient**: Library for interacting with Google APIs.

## Prerequisites

Make sure you have the Google pip and the correct version of Python installed.

### Installing Google pip

```
pip install google-auth google-auth-oauthlib google-api-python-client
```

## Configuration

Before getting started, you need to set up authentication credentials with Google.

1. Create a project in the [Google Cloud Console](https://console.cloud.google.com/).
2. Enable the Google Sheets API for your project.
3. Create a JSON credentials file for the type of authentication you want to use (e.g., OAuth2).
4. Rename the credentials file to `credentials.json` and place it in the root directory of the project.

## Usage

Run the `main.py` script to insert data into the Google Sheets.

```bash
python main.py
```

