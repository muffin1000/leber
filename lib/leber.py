import json
import requests
import random

class Login:
    def __init__(self, user_id: int, phone: str, passwd: str):
        self.user_id = user_id
        self.phone = f'{phone[:0]}+81{phone[1:]}'
        self.passwd = passwd
        self.token, self.patients_id, self.company_id, self.error = None, None, None, None
        self.get_user_info()

    def get_user_info(self) -> None:
        url = 'https://api.leber11.com/v9//users/sign_in'
        headers = { 'Content-Type': 'application/json' }
        content = json.dumps({ 'login': self.phone, 'password': self.passwd }).encode('utf-8')
        re = requests.post(url, headers=headers, data=content)
        json_re = json.loads(re.text)
        try:
            self.token = json_re['result']['user']['authentication_token']
            self.patients_id = json_re['result']['user']['patients'][0]['id']
            self.company_id = json_re['result']['user']['patients'][0]['company_id']
        except:
            sever_status = f'{re.status_code} ✅' if re.status_code == 200 else f'{re.status_code} ❌'
            self.error = f'Server Status: {sever_status}\nResponse: {json_re["message"]}'

class Submit(Login):
    def __init__(self, company_id:str, user_id: int, patients_id: str, token: str):
        self.company_id = company_id
        self.user_id = user_id
        self.patients_id = patients_id
        self.token = token
        self.set_temp()
        self.norm, self.error = None, None

    def set_temp(self):
        self.temp_id = random.randint(21, 27)
        self.temp = round(0.1 * float(self.temp_id) + 33.9, 1)

    def exec(self):
        url = f'https://api.leber11.com/v9//patients/{self.patients_id}/submit_temperatures'
        headers = {
            'Content-Type' : 'application/json',
            'X-USER-TOKEN': self.token
        }
        content = json.dumps({
            'company_id': self.company_id,
            'temp_answers_attributes': [
                {
                    'answer_id': [self.temp_id],
                    'question_id':1,
                    'question_number':1,
                    'additional_comment':''
                },
                {
                    'answer_id':[119],
                    'question_id':2,
                    'question_number':2,
                    'additional_comment':''
                },
                {
                    'answer_id':[136],
                    'question_id':3,
                    'question_number':3,
                    'additional_comment':''
                }
            ]
        }).encode('utf-8')
        re = requests.post(url, data=content, headers=headers)
        json_re = json.loads(re.text)
        if json_re['status'] != 1 or re.status_code != 200:
            self.error = f'server staus: {re.status_code}\nError: {json_re["message"]}'
        else:
            self.norm = f'Response: {json_re["message"]}\nBody temperature: {self.temp}'

