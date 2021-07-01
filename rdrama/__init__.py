import requests

token_path = '/tmp/ruqqus_token'

class Drama:
    def __init__(self, client_id, client_secret, user_agent, access_token, refresh_token,x_user_type='Bot'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.x_user_type = x_user_type
        self.auth_header = f"Bearer {self.access_token}"
        self.headers = {"Authorization": self.auth_header, "User-Agent": self.user_agent,"X-User-Type": self.x_user_type}
        self.base_url = "https://rdrama.net/{}"

    def request(self, method, endpoint, data):
        self.endpoint = endpoint.split('/',1)[1]
        self.url = self.base_url.format(self.endpoint)
        response = requests.request(method,self.url,headers=self.headers,data=data)
        self.status_code = response.status_code
        self.response_reason = response.reason
        if self.status_code in [200,204]:
            return response.json()
        else:
            raise Exception(f"{self.status_code}/{self.response_reason} on endpoint {self.endpoint}")

    def get(self, endpoint, data=None):
        return self.request('GET', endpoint, data=data)
    
    def post(self, endpoint, data=None):
        return self.request('POST', endpoint, data=data)
