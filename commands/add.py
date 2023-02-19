from lib.leber import Login
from setting import *
from lib.db import DB
import time

@tree.command(
    name='add',
    description='DBに追加'
)
async def login(interaction: discord.Interaction, phone: str, passwd: str):
    user_data = Login(interaction.user.id, phone, passwd)
    if user_data.error is None:
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO     get {interaction.user.name} token successfully')
        embed = discord.Embed(
            title='成功',
            description='ログインに成功',
            color=discord.Colour.green()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        time.sleep(1)
        db = DB()
        if any([item[1] == interaction.user.id for item in db.get_all_data()]):
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ERROR     already {interaction.user.name} is in DB')
            embed = discord.Embed(
                title='エラー',
                description='すでにDBに追加されています',
                color=discord.Colour.red()
            )
            await interaction.edit_original_response(embed=embed)

        else:
            db.add_to_db(user_data.company_id, interaction.user.id, user_data.patients_id, user_data.token, user_data.phone, user_data.passwd)
            print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO     add db {interaction.user.name}')
            embed = discord.Embed(
                title='成功',
                description='DBに追加されました。',
                color=discord.Colour.green()
            )
            await interaction.edit_original_response(embed=embed)

    else:
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ERROR     {user_data.error}')
        embed = discord.Embed(
            title='エラー',
            description=user_data.error,
            color=discord.Colour.red()
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)