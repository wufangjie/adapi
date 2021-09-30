import requests
from .conf import domain_dict, token_url_dict, host_url_dict


class Auth:

    def __init__(self, client_id, client_secret, refresh_token, region):
        self.client_id = client_id
        self.client_secret = client_secret
        self.refresh_token = refresh_token
        self.region = region
        self.domain = domain_dict[self.region]
        self.token_url = token_url_dict[self.region]
        self.headers = {
            "Content_Type": "application/x-www-form-urlencoded:charset=UTF-8"
        }
        self.uri_path = ""

    def get_new_access_token(self):
        data = {
            "grant_type": "refresh_token",
            "refresh_token": self.refresh_token,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.token_url, data, headers=self.headers)
        result = response.json()
        self.access_token = result["access_token"]

    def get_grant_url(self, redirect_uri):
        host_url = host_url_dict[self.region]
        scope = "cpc_advertising:campaign_management"
        response_type = "code"
        temp = "{}?client_id={}&scope={}&response_type={}&redirect_uri={}"
        return temp.format(
            host_url, self.client_id, scope, response_type, redirect_uri)

    def get_refresh_token(self, code):
        """NOTE: only for the first time using api"""
        data = {
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": self.redirect_uri,
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        response = requests.post(self.token_url, data, headers=self.headers)
        result = response.json()
        self.access_token = result["access_token"]
        self.refresh_token = result["refresh_token"]
