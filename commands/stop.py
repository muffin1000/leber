from setting import *
from lib.db import DB
@tree.command(
    name='stop',
    description='検温の自動送信中止'
)
async def stop(interaction: discord.Interaction):
    try:
        db = DB()
        db.stop_submit(interaction.user.id)
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO    {interaction.user.name} stops submit')
        embed = discord.Embed(
            title='成功',
            description='検温は停止されます',
            color=discord.Colour.green()
        )
        await interaction.response.send_message(embed=embed)        
    except Exception as e:
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ERROR    change failed {interaction.user.name} data.{e}')
        embed = discord.Embed(
            title='エラー',
            description='停止に失敗しました',
            color=discord.Colour.red()
        )
        await interaction.response.send_message(embed=embed)  