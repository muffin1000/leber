#! /usr/local/bin/python3
from  setting import *
import commands.add as add
import commands.rm as rm
import commands.stop as stop
import commands.status as status
import commands.help as help
from auto_submit import *

@client.event
async def on_ready():
    print('on ready')
    await tree.sync()
    auto_submit.start()

client.run(token)