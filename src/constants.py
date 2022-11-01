import json

API = "twitch"

ACCESS_TOKEN = None
ACCESS_TOKEN_KEY = f"{API}_access_token"
API_TOKEN_FILE_PATH = "/Users/amandate/Development/Projects/Utilities/api_tokens.json"
CLIENT_ID = None
CLIENT_ID_KEY = f"{API}_client_id"
CLIENT_SECRET = None
CLIENT_SECRET_KEY = f"{API}_client_secret"
USER_ID = None
USER_ID_KEY = f"{API}_user_id"

GET_USER_FOLLOWERS_API_CALL = \
    f"curl -X GET 'https://api.twitch.tv/helix/users/follows?to_id={USER_ID}' \
    -H 'Authorization: Bearer {ACCESS_TOKEN}' \
    -H 'Client-Id: {CLIENT_ID}'"

def set_constants():
    json_file = open(API_TOKEN_FILE_PATH)
    json_data = json.load(json_file)

    global CLIENT_ID, CLIENT_SECRET, ACCESS_TOKEN, USER_ID
    CLIENT_ID = json_data[CLIENT_ID_KEY]
    CLIENT_SECRET = json_data[CLIENT_SECRET_KEY]
    ACCESS_TOKEN = json_data[ACCESS_TOKEN_KEY]
    USER_ID = json_data[USER_ID_KEY]