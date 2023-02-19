from lib.db import DB
from setting import *

@tree.command(
    name='rm',
    description='DBから削除'
)
async def remove(interaction: discord.Interaction):
    db = DB()
    try:
        db.remove_data(interaction.user.id)
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} INFO    {interaction.user.name} data was removed from DB')
        embed = discord.Embed(
            title='成功',
            description='DBからデータ削除をしました',
            color=discord.Colour.green()
        )
        await interaction.response.send_message(embed=embed)
    except Exception as e:
        print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S")} ERROR    removing failed {interaction.user.name} data.\n{e}')
        embed = discord.Embed(
            title='エラー',
            description='DBからのデータ削除に失敗しました。',
            color=discord.Colour.red()
        )
        await interaction.response.send_message(embed=embed)