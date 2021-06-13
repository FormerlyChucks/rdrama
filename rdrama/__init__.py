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
        auth_header = "Bearer {}".format(open(self.token_file,'r+').read().replace("\n",""))
        headers = {"Authorization": auth_header, "User-Agent": self.user_agent,"X-User-Type": str(self.x_user_type)}
        endpoint = endpoint.split('/',1)[1]
        url = 'https://rdrama.net/{}'.format(endpoint)
        response = requests.request(method,url,headers=headers,data=data)
        self.status_code = response.status_code
        if self.status_code == 200:
            return response.json()
        elif self.status_code == 204:
            return self.status_code
        else:
            raise Exception('{}/{} on endpoint: {}'.format(response.status_code,response.reason,endpoint))

    def get(self, endpoint, data=None):
        return self.request('GET', endpoint, data=data)
    
    def post(self, endpoint, data=None):
        return self.request('POST', endpoint, data=data)
