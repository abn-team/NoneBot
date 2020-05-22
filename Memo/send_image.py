from nonebot import on_command, CommandSession, MessageSegment
import requests
import os
import random
import re

path = os.path.abspath(os.curdir)+r"\image"


@on_command('fox', only_to_me=False)
async def fox(session: CommandSession):
    try:
        web_image = requests.get('https://foxrudor.de/', timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\fox.jpg", "wb") as f:
                f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image("file:///"+path+r"\fox.jpg")))


@on_command('edgecat', only_to_me=False)
async def edgecat(session: CommandSession):
    try:
        web_image = requests.get('http://edgecats.net/', timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\edgecat.gif", "wb") as f:
                f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image("file:///"+path+r"\edgecat.gif")))


@on_command('waifu', only_to_me=False)
async def waifu(session: CommandSession):
    waifu_url = 'https://www.thiswaifudoesnotexist.net/example-' + \
        str(random.randint(1, 99999))+'.jpg'
    try:
        web_image = requests.get(waifu_url, timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\waifu.jpg", "wb") as f:
                f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image("file:///"+path+r"\waifu.jpg")))


@on_command('cat', only_to_me=False)
async def cat(session: CommandSession):
    try:
        web_image = requests.get(
            'https://thiscatdoesnotexist.com/', timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\cat.jpg", "wb") as f:
                f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image("file:///"+path+r"\cat.jpg")))


@on_command('吸', only_to_me=False)
async def 吸(session: CommandSession):
    User_ID = re.match(r'([0-9]+)|\[CQ:at,qq=([0-9]+)\]', session.current_arg)
    User_ID = User_ID.group(2) if User_ID.group(2) else User_ID.group(1)
    if User_ID == None:
        session.finish('获取失败，请@或者输入对象Q号')
    try:
        web_image = requests.get(
            "https://q1.qlogo.cn/g?b=qq&nk=%s&s=640" % User_ID, timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\avatar.jpg", "wb") as f:
                f.write(web_image.content)
            session.finish(str(MessageSegment.image(
                "file:///"+path+r"\avatar.jpg")))
        else:
            session.finish('获取头像失败')
    except:
        pass


@on_command('壁纸', only_to_me=False)
async def 壁纸(session: CommandSession):
    try:
        web_image = requests.get(
            'https://uploadbeta.com/api/pictures/random/?key=BingEverydayWallpaperPicture', timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\BingEverydayWallpaper.jpg", "wb") as f:
                f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image(
        "file:///"+path+r"\BingEverydayWallpaper.jpg")))


@on_command('acg壁纸', only_to_me=False)
async def acg壁纸(session: CommandSession):
    try:
        web = requests.get(
            "http://api.mtyqx.cn/api/random.php?return=json").json()
        web_image = requests.get(web['imgurl'], timeout=10)
        if web_image.status_code == 200:
            with open(path+r"\AcgWallpaper.jpg", "wb") as f:
                f.write(web_image.content)
        else:
            web = requests.get(
                "http://api.mtyqx.cn/tapi/random.php?return=json").json()
            web_image = requests.get(web['imgurl'], timeout=10)
            if web_image.status_code == 200:
                with open(path+r"\AcgWallpaper.jpg", "wb") as f:
                    f.write(web_image.content)
    except:
        pass
    session.finish(str(MessageSegment.image(
        "file:///"+path+r"\AcgWallpaper.jpg")))


@on_command('pixiv', only_to_me=False)
async def pixiv(session: CommandSession):
    send=True
    params = {
        # "apikey":"",
        "r18": 0,
        "keyword": "",
        "size1200": True
    }
    params['keyword'] = session.current_arg_text.split()
    try:
        web = requests.get('https://api.lolicon.app/setu/',
                           params=params).json()
        if web['code'] != 0:
            await session.send(web['msg'])
        else:
            await session.send(f"PID:{str(web['data'][0]['pid'])}\n若图片发不出来请自行查看")
            web_image = requests.get(web['data'][0]['url'], timeout=10)
            if web_image.status_code == 200:
                with open(path+r"\Pixiv.jpg", "wb") as f:
                    f.write(web_image.content)
            await session.send(str(MessageSegment.image("file:///"+path+r"\Pixiv.jpg")))
    except:
        pass
    session.finish()
