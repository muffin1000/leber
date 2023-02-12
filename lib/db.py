import sqlite3
from setting import dbname, tablename

class DB:
    def add_to_db(self, company_id: str, user_id: int, patients_id: str, token: str, phone: str, passwd: str):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            phone = phone.replace('+', '\+')
            cur.execute(f'INSERT INTO {tablename}(company_id, discord_id, patients_id, token, phone, passwd, bool) VALUES (?, ?, ?, ?, ?, ?, ?)', (company_id, user_id, patients_id, token,  phone, passwd, 1))
            db.commit()

    def stop_submit(self, user_id: int):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute(f'UPDATE {tablename} SET bool = 0 WHERE "discord_id" = {user_id}')
            db.commit()

    def get_all_data(self):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute(f'SELECT * FROM {tablename}')
            all_data = cur.fetchall()
        return all_data
    
    def remove_data(self, user_id):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute(f'DELETE FROM {tablename} WHERE "discord_id" = {user_id}')
    
    def init_bool(self):
        with sqlite3.connect(dbname) as db:
            cur = db.cursor()
            cur.execute(f'UPDATE {tablename} SET bool = 1 WHERE bool = 0')