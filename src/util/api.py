import requests

from setting import HEADERS_DEFAULT

POST = "POST"
GET = "GET"

class BFWBAPIClient:
    def __init__(self, api_site, endpoint="", headers=HEADERS_DEFAULT, proxies=None):
        self.client = requests.Session()
        self.api_site = api_site
        self.headers = headers
        self.proxies = proxies
        self.endpoint = endpoint

    def post(self, endpoint="", **kwargs):
        endpoint = endpoint if endpoint else self.endpoint
        url = f'{self.api_site}/{endpoint}' if endpoint else self.api_site
        return self.client.post(url, headers=self.headers, proxies=self.proxies, **kwargs)

    def get(self, endpoint="", **kwargs):
        endpoint = endpoint if endpoint else self.endpoint
        url = f'{self.api_site}/{endpoint}' if endpoint else self.api_site
        return self.client.post(url, headers=self.headers, proxies=self.proxies, **kwargs)

    def call(self, method, endpoint, **kwargs):
        endpoint = endpoint if endpoint else self.endpoint
        http_method = {
            POST: self.post,
            GET: self.get
        }
        http_method.get(method)(endpoint, **kwargs)

    def close(self):
        self.client.close()
