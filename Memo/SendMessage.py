import nonebot
import json

async def data_reset():
    f = open('server.json','w')
    f.write(json.dumps([]))
    f.close()


@nonebot.scheduler.scheduled_job('interval', minutes=1)
async def _():
    bot = nonebot.get_bot()
    f = open('server.json','r')
    data = json.load(f)
    f.close()
    try:
        if data == []:
            pass
        else:
            try:
                for error in data:
                    error = dict(error)
                    #message = '[CQ:at,qq={}]\n{}'.format(error['user_id'],error['message'])
                    await bot.send_private_msg(user_id=error['user_id'],message=error['message'])
            except:
                await bot.send_private_msg(user_id=350311089, message='发现未知错误,数据已重置')
            await data_reset()
    except:
        await bot.send_private_msg(user_id=350311089, message='发现未知错误,数据已重置')
        await data_reset()