from setting import *

@tree.command(
    name='help',
    description='helpコマンドの表示'
)
async def help(interaction: discord.Interaction):
    embed = discord.Embed(
        title='helpコマンド',
        description='helpコマンドの表示',
        color=discord.Colour.blue()
    )
    embed.add_field(
        name='addコマンド',
        value='自動送信に参加'
    )
    embed.add_field(
        name='rmコマンド',
        value='自動送信から削除(個人情報は削除されます)'
    )
    embed.add_field(
        name='stopコマンド',
        value='その日の検温の自動送信の停止'
    )
    embed.add_field(
        name='statusコマンド',
        value='BotサーバとLEBERの状況を表示'
    )
    await interaction.response.send_message(embed=embed)