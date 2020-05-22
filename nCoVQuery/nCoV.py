import requests
import json
from nonebot import on_command, CommandSession


async def nCovProvince(province):
    url = "https://3g.dxy.cn/newh5/view/pneumonia"
    try:
        data = requests.get(url)
        data.encoding = "utf-8"
        data = data.text
        Adata = data[data.find("window.getStatisticsService"):]
        Adata = Adata[Adata.find("=")+2:Adata.find(r'catch(e){}')-1]
        Adata = json.loads(Adata)
        Pdata = data[data.find('window.getAreaStat'):]
        Pdata = Pdata[Pdata.find("=")+2:Pdata.find(r'catch(e){}')-1]
        Pdata = json.loads(Pdata)
        message = ""
        provinceMessage = ""
        try:
            a = Adata['confirmedIncr']
        except:
            Adata['confirmedIncr'] = 0
        try:
            a = Adata['suspectedIncr']
        except:
            Adata['suspectedIncr'] = 0
        try:
            a = Adata['seriousIncr']
        except:
            Adata['seriousIncr'] = 0
        try:
            a = Adata['deadIncr']
        except:
            Adata['deadIncr'] = 0
        try:
            a = Adata['curedIncr']
        except:
            Adata['curedIncr'] = 0
        if Adata['confirmedIncr'] == 0 and Adata['suspectedIncr'] == 0 and Adata['seriousIncr'] == 0 and Adata['deadIncr'] == 0 and Adata['curedIncr'] == 0:
            message = "\n未能获取到与昨日比较数据"
        for provinceState in Pdata:
            if provinceState["provinceName"] == province or provinceState["provinceShortName"] == province:
                provinceMessage = "\n" + \
                    provinceState["provinceName"]+":\n确诊[" + \
                    str(provinceState["confirmedCount"])+"]例"
                if provinceState["deadCount"] != 0:
                    provinceMessage += "\n死亡[" + \
                        str(provinceState["deadCount"])+"]例"
                if provinceState["curedCount"] != 0:
                    provinceMessage += "\n治愈[" + \
                        str(provinceState["curedCount"])+"]例"
                break
        message = "全国数据:\n确诊["+str(Adata['confirmedCount'])+"]例+"+str(Adata['confirmedIncr']) + "\n疑似["+str(Adata['suspectedCount'])+"]例+"+str(Adata['suspectedIncr'])+"\n重症["+str(
            Adata['seriousCount'])+"]例+"+str(Adata['seriousIncr']) + "\n死亡["+str(Adata['deadCount'])+"]例+"+str(Adata['deadIncr'])+"\n治愈["+str(Adata['curedCount'])+"]例+"+str(Adata['curedIncr'])+message+provinceMessage
        return message
    except:
        return '信息获取失败，请稍后再试'


@on_command('nCov', aliases=('ncov', '疫情'), only_to_me=False)
async def nCov(session: CommandSession):
    session.state['province'] = session.current_arg_text.strip()
    province = session.get('province')
    message = await nCovProvince(province)
    session.finish(message)
