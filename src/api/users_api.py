from api.twitch_api import TwitchAPI
from constants.endpoints import *
from constants.parameter_keys import TO_ID_KEY

"""
    Represents interaction with the Twitch Users API.
"""

class TwitchUsersAPI(TwitchAPI):
    def __init__(self, client_id, access_token=None):
        super().__init__(client_id, access_token)
        self.base_endpoint = f"{HELIX_ENDPOINT}{USERS_ENDPOINT}"
        self.follows_endpoint = f"{self.base_endpoint}{FOLLOWS_ENDPOINT}"

    '''
        Sends a GET request to the Twitch User Followers API for the 
        given user_id and params and returns the json response.
    '''
    def getUserFollowers(self, user_id, params=None):
        endpoint = f"{self.follows_endpoint}?{TO_ID_KEY}={user_id}"
        return self._request_get(endpoint, params)