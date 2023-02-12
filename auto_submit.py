from setting import *
from lib.db import DB
from lib.leber import Submit
@tasks.loop(seconds=10)
@client.event
async def auto_submit():
    db = DB()
    for item in db.get_all_data():
        submit = Submit(*item[:4])
        if item[-1]: submit.exec()
        if submit.error is None:
            user = await client.fetch_user(item[1])
            embed = discord.Embed(
                title='成功',
                description=submit.norm,
                color=discord.Color.green()
            )
            await user.send(embed=embed)
        else:
            user = await client.fetch_user(item[1])
            embed = discord.Embed(
                title='エラー',
                description=submit.error,
                color=discord.Color.red()
            )
            await user.send(embed=embed)
    db.init_bool()