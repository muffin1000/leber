from setting import *

@tree.command(
    name='help',
    description='helpコマンドの表示'
)
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title='help',
        description='helpの表示',
        color=discord.Colour.blue()
    )
    embed.add_field(
        name='add',
        value='自動送信に参加',
        inline=False
    )
    embed.add_field(
        name='rm',
        value='自動送信から削除(個人情報は削除されます)',
        inline=False
    )
    embed.add_field(
        name='stop',
        value='その日の検温の自動送信の停止',
        inline=False
    )
    embed.add_field(
        name='status',
        value='BotサーバとLEBERの状況を表示',
        inline=False
    )
    await interaction.response.send_message(embed=embed)