import requests

class TwitchAPI:
    def __init__(self, client_id, access_token=None):
        self.client_id = client_id
        self.access_token = access_token

    def _get_request_headers(self):
        headers = {
            "Client-ID": self.client_id,
        }

        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        return headers

    def _request_get(self, endpoint, params=None, json=True):
        headers = self._get_request_headers()
        get_response = requests.get(endpoint, params=params, headers=headers)
        
        if json:
            return get_response.json()
        return get_response