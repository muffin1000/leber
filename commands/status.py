from setting import *
from lib.status import *

@tree.command(
    name='status',
    description='ステータスの確認'
)
async def status(interaction: discord.Interaction):
    print(f'status command from {interaction.user.id}')
    status = Status()
    embed = discord.Embed(
        title='Status',
        description=f'BotサーバのCPU使用率: {status.load}\nLEBERの状況{status.server_status}',
        color=discord.Colour.blue()
    )
    await interaction.response.send_message(embed=embed)