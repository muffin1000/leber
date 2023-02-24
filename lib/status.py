import psutil
import requests

def get_server_status():
    url = 'https://api.leber11.com/v9//users/sign_in'
    re = requests.post(url)
    return re.status_code

load = f'{psutil.cpu_percent(interval=1)}%'
server_status = get_server_status()