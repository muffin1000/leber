import psutil
from enum import Enum
import requests



class Status:
    def __init__(self) -> None:
        self.load = f'{psutil.cpu_percent(interval=1)}%'
        self.server_status = self.get_server_status()

    def get_server_status():
        url = 'https://api.leber11.com/v9//users/sign_in'
        re = requests.post(url)
        return re.status_code
