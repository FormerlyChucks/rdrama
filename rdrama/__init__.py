import requests

class Drama:
    def __init__(self, client_id, client_secret, user_agent, access_token, refresh_token,x_user_type='Bot'):
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
        self.refresh_token = refresh_token
        self.access_token = access_token
        self.x_user_type = x_user_type

    def request(self, method, endpoint, data):
        self.headers = {"Authorization": f"Bearer {self.access_token}", "User-Agent": self.user_agent,"X-User-Type": self.x_user_type}
        self.url = f"https://rdrama.net/{endpoint.split('/',1)[1]}"
        response = requests.request(method,self.url,headers=self.headers,data=data)
        self.status_code = response.status_code
        self.response_reason = response.reason
        if self.status_code == 200:
            return response.json()
        if self.status_code == 204:
            return self.status_code
        else:
            raise Exception(f"{self.status_code}/{self.response_reason} on endpoint {endpoint}")

    def get(self, endpoint, data=None):
        return self.request('GET', endpoint, data=data)

    def post(self, endpoint, data=None):
        return self.request('POST', endpoint, data=data)
