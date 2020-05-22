from nonebot import on_command, CommandSession
import os


def SaveList(data, fileID):
    fileID = 'memo\\'+str(fileID)+'.txt'
    if os.path.exists('memo') == False:
        os.mkdir('memo')
    f = open(fileID, "a")
    f.write(data+"\n")
    f.close()


def ReadList(fileID):
    fileID = 'memo\\'+str(fileID)+'.txt'
    if os.path.exists('memo') == False:
        os.mkdir('memo')
    try:
        f = open(fileID, "r")
    except :
        f = open(fileID, "w")
        f.close()
        return []
    data = []
    data = f.read()
    data = data.splitlines()
    f.close()
    try:
        removeNum = data.count('')
        for i in range(removeNum):
            data.remove('')
    except:
        pass
    return data


def DelList(number, data, fileID):
    del data[number]
    fileID = 'memo\\'+str(fileID)+'.txt'
    if os.path.exists('memo') == False:
        os.mkdir('memo')
    f = open(fileID, "w")
    for w in data:
        f.write(w+"\n")
    f.close()


@on_command('SaveMemo', aliases=('memoadd', '添加备忘录'), only_to_me=False)
async def SaveMemo(session: CommandSession):
    user_id = session.ctx['user_id']
    session.state['memo'] = session.current_arg_text.strip()
    memo = session.get('memo', prompt='请输入你要添加的备忘录')
    try:
        SaveList(memo, user_id)
    except:
        session.finish('储存失败')
    session.finish('已储存至备忘录')


@on_command('ReadMemo', aliases=('memo', '读取备忘录', 'readmemo'), only_to_me=False)
async def ReadMemo(session: CommandSession):
    user_id = session.ctx['user_id']
    try:
        user_name = session.ctx['sender']['card']
    except:
        user_name = session.ctx['sender']['nickname']
    read = ReadList(user_id)
    if read == []:
        session.finish('无备忘录记录')
    message = user_name+"的备忘录记录为："
    memonum = 0
    for m in read:
        message += "\n["+str(memonum)+"]"+m
        memonum += 1
    session.finish(message)


@on_command('DelMemo', aliases=('memodel', '删除备忘录', 'delmemo'), only_to_me=False)
async def DelMemo(session: CommandSession):
    user_id = session.ctx['user_id']
    session.state['delmemo'] = session.current_arg_text.strip()
    delmemo = session.get('delmemo', prompt='请输入你要删除的备忘录序号')
    try:
        delmemo = int(delmemo)
    except:
        session.finish('请输入数字')
    read = ReadList(user_id)
    if delmemo > len(read) - 1:
        session.finish('超出范围，删除失败')
    else:
        try:
            DelList(delmemo, read, user_id)
        except:
            session.finish('删除失败')
        session.finish('删除备忘录成功')


@on_command('HelpMemo', aliases=('memohelp','备忘录帮助'), only_to_me=False)
async def HelpMemo(session: CommandSession):
    message = '#memoadd [备忘录内容]\n#添加备忘录 [备忘录内容]  添加备忘录\n#memo 读取备忘录 \n#readmemo  读取备忘录\n#memodel [序号]\n#删除备忘录 [序号]\n#delmemo [序号]  删除备忘录\n示例：\n#memoadd 这是一条备忘录\n#memodel 0'
    session.finish(message)