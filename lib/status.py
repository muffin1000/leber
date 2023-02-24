import requests

def get_server_status():
    url = 'https://api.leber11.com/v9//users/sign_in'
    re = requests.post(url)
    return re.status_code

server_status = get_server_status()