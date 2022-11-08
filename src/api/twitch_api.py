import requests

"""
    Represents interaction with the Twitch API.
"""

class TwitchAPI:
    def __init__(self, client_id, access_token=None):
        self.client_id = client_id
        self.access_token = access_token

    '''
        Returns the headers to be used when making calls to the API.
    '''
    def _get_request_headers(self):
        headers = {
            "Client-ID": self.client_id,
        }

        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        return headers

    '''
        Sends a GET request to the given endpoint and params and returns its
        response.
    '''
    def _request_get(self, endpoint, params=None, json=True):
        headers = self._get_request_headers()
        get_response = requests.get(endpoint, params=params, headers=headers)
        
        if json:
            return get_response.json()
        return get_response