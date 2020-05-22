from nonebot import on_command, CommandSession


async def Save(message):
    f=open("message.txt","w")
    f.write(message)
    f.close()


@on_command('Write', aliases=('write', '写入'))
async def Write(session: CommandSession):
    session.state['message'] = session.current_arg_text.strip()
    message = session.get('message', prompt='请输入你要储存的信息')
    await Save(message)
    session.finish("已储存")