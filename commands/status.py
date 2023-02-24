from setting import *
from lib.status import *

@tree.command(
    name='status',
    description='ステータスの確認'
)
async def status(interaction: discord.Interaction):
    print(f'status command from {interaction.user.id}')
    embed = discord.Embed(
        title='Status',
        description=f'{Status.load.value}\n{Status.server_status.value}',
        color=discord.Colour.blue()
    )
    await interaction.response.send_message(embed=embed)