import psutil
from enum import Enum
import requests

def get_server_status():
    url = 'https://api.leber11.com/v9//users/sign_in'
    re = requests.post(url)
    return re.status_code

class Status(Enum):
    load = f'{psutil.cpu_percent(interval=1)}%'
    server_status = get_server_status()


print(Status.server_status.value)