from nonebot import on_command, CommandSession, permission
import os
import subprocess
import sys


@on_command('overload')
async def overload(session: CommandSession):
    path = os.path.abspath(os.curdir)
    subprocess.Popen("cd %s&&timeout /T 5&&python bot.py" %
                     path, shell=True, creationflags=subprocess.CREATE_NEW_CONSOLE)
    await session.send('执行成功，5秒后会重启')
    sys.exit(0)


@on_command('kill', permission=permission.SUPERUSER)
async def kill(session: CommandSession):
    await session.send('关闭中')
    sys.exit(0)
    session.finish('关闭失败')
