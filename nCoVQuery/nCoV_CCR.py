import requests
import json
from nonebot import on_command, CommandSession


async def ncov_city(inp):

    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    try:
        data = requests.get(url)
    except:
        return False
    data.encoding = "utf-8"
    data = data.text
    data = data[data.find('window.getAreaStat'):]
    data = data[data.find("=")+2:data.find(r'catch(e){}')-1]
    data = json.loads(data)

    res_data = [{'name': '全国', 'cfm': 0, 'cur': 0, 'ded': 0}, {
        'name': '省份', 'cfm': 0, 'cur': 0, 'ded': 0}, {'name': '城市', 'cfm': 0, 'cur': 0, 'ded': 0}]

    for i in data:
        for j in i['cities']:
            if j['cityName'] == inp:
                res_data[2]['name'] = j['cityName']
                res_data[2]['cfm'] = j["confirmedCount"]
                res_data[2]['cur'] = j["curedCount"]
                res_data[2]['ded'] = j["deadCount"]

                res_data[1]['name'] = i['provinceName']
                res_data[1]['cfm'] = i["confirmedCount"]
                res_data[1]['cur'] = i["curedCount"]
                res_data[1]['ded'] = i["deadCount"]

        res_data[0]['cfm'] += i["confirmedCount"]
        res_data[0]['cur'] += i["curedCount"]
        res_data[0]['ded'] += i["deadCount"]

    message = ''

    for k in res_data:
        message += proc_data_city(k)

    return message


def proc_data_city(data_dict):

    message = '\n'+data_dict['name']+'数据：'

    if data_dict['cfm'] != 0:
        message += "\n\t确诊[" + \
            str(data_dict["cfm"]) + "]例"

    if data_dict['cur'] != 0:
        message += "\n\t治愈[" + \
            str(data_dict["cur"]) + "]例"

    if data_dict['ded'] != 0:
        message += "\n\t死亡[" + \
            str(data_dict["ded"]) + "]例"

    return message


@on_command('nCovcty', aliases=('ncovcty', '城市疫情'), only_to_me=False)
async def nCovGo(session: CommandSession):
    session.state['city'] = session.current_arg_text.strip()
    inp = session.get('city', prompt='请输入你要查询的城市')
    message = await ncov_city(inp)
    if message == False:
        message = '数据获取失败'
    else:
        message = message[message.find('\n')+1:]
    session.finish(message)
