from nonebot import on_command, CommandSession
import os


def call_cmd(path):
    try:
        info = os.popen('cd %s && git fetch --all && git reset --hard origin/master && git pull origin master' %
                        path).read()
        return '更新成功\n%s' % info
    except:
        return '更新失败，超时或未知错误'


@on_command('Pull_Web', aliases=('git_pull_web', '更新web'), only_to_me=False)
async def Pull_Web(session: CommandSession):
    path = r'C:\Users\Administrator\Desktop\abn_crypt'
    info = call_cmd(path)
    session.finish(info)


@on_command('Pull_Bot', aliases=('git_pull_bot', '更新bot'), only_to_me=False)
async def Pull_Bot(session: CommandSession):
    path = os.path.abspath(os.curdir)
    info = call_cmd(path)
    session.finish(info)
