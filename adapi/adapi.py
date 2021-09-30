import requests
from .conf import domain_dict
import json


class ProClient(object):
    def __init__(self, auth):
        self.auth = auth
        self.domain = domain_dict[self.auth.region]
        self.method = "get"
        self.data = None
        self.uri_path = None

        self.headers = {
            "Content-Type": "application/json",
            "Amazon-Advertising-API-ClientId": self.auth.client_id
        }
        self.headers_gzip = {
            "Accept-encoding": "gzip",
            "Amazon-Advertising-API-ClientId": self.auth.client_id
        }
        self.update_access()

    def update_access(self):
        self.auth.get_new_access_token()
        self.access_token = self.auth.access_token
        temp = "Bearer {}".format(self.access_token)
        self.headers["Authorization"] = temp
        self.headers_gzip["Authorization"] = temp

    def execute(self):
        url = self.domain + self.uri_path
        if self.method == "delete":
            response = requests.delete(url, headers=self.headers).text
            return response
        if self.data:
            self.data = json.dumps(self.data)
        response = requests.request(
            self.method, url, headers=self.headers, data=self.data)
        self.data = None # remove data when used
        try:
            return response.json()
        except:
            # sometime the .json() will raise and Exception.
            return response

    def execute_download(self, url):
        return requests.Session().get(url, headers=self.headers_gzip)


class Client(ProClient):
    def __init__(self, auth):
        if not hasattr(auth, 'profile_id'):
            raise Exception('No profile_id found!')
        self.profile_id = auth.profile_id
        super(Client, self).__init__(auth)
        self.headers["Amazon-Advertising-API-Scope"] = self.profile_id
        self.headers_gzip["Amazon-Advertising-API-Scope"] = self.profile_id
