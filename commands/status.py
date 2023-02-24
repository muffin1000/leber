from setting import *
from lib.status import *
import psutil
@tree.command(
    name='status',
    description='ステータスの確認'
)
async def status(interaction: discord.Interaction):
    print(f'status command from {interaction.user.id}')
    embed = discord.Embed(
        title='Status',
        description=
        f'BotサーバのCPU使用率: {psutil.cpu_percent(interval=1)}%\
        \nBotサーバのメモリ使用率: {psutil.virtual_memory().percent}\
        \nLEBERの状況: {server_status}',
        color=discord.Colour.blue()
    )
    await interaction.response.send_message(embed=embed)