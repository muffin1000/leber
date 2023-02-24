import requests

def get_server_status():
    url = 'https://api.leber11.com/v9//users/sign_in'
    re = requests.post(url)
    msg = f'{re.status_code}🟢' if re.status_code == 200 else f'{re.status_code}❌'
    return msg

server_status = get_server_status()