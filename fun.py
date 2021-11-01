import json
import requests
from setting import *

#获取用户基本信息
def getuserInfo():
    try:
        response1 = requests.get(url="https://api.bilibili.com/x/web-interface/nav", headers=headers)
        response1 = json.loads(response1.text)
        currentlevel = str(response1['data']['level_info']['current_level'])
        current_min = response1['data']['level_info']['current_min']
        current_exp = response1['data']['level_info']['current_exp']
        next_exp = response1['data']['level_info']['next_exp']
        money = str(response1['data']['money'])
        vip = response1['data']["vip_label"]["text"]
        mid = str(response1['data']["wallet"]["mid"])
        bcoin_balance = str(response1['data']["wallet"]["bcoin_balance"])
        print(f"你的当前等级是{currentlevel}, 当前经验为{current_exp}, 离下一级还有{current_min}, 下一级共需{next_exp}")
        print(f"现在还有{money}硬币, 是{vip}, B币余额为{bcoin_balance}")
    except AttributeError:
        print("发生错误，错误信息：" + {response1.text})

def liveSign():
        try:
            response = requests.get(url='https://api.live.bilibili.com/xlive/web-ucenter/v1/sign/DoSign', headers=headers)
            print('直播签到:'+json.loads(response.text)['message'])
        except:
            print('直播签到失败,发生未知错误')

def comicSign():
    try:
        data = {
             "platform": 'ios'
        }
        res = requests.post(url='https://manga.bilibili.com/twirp/activity.v1.Activity/ClockIn', headers=headers, data=data)
        if json.loads(res.text)['code'] == 0:
            print('漫画签到成功')
        else:
            print('漫画签到失败:' + res.json()['msg'])
    except:
        print('漫画签到异常')

def getHotVideo():
    try:
        res = requests.get(url='https://api.bilibili.com/x/web-interface/popular?ps=50&pn=1', headers=headers)
        video_list = []
        for i in json.loads(res.text)['data']['list']:
            video_list.append({'aid':i['aid'],'cid':i['cid']})
            hotVideo_aidlist = video_list
        return hotVideo_aidlist
    except:
        print("获取热门视频列表失败")

def getCoinTodayExp():
    res = requests.get(url="https://api.bilibili.com/x/web-interface/coin/today/exp", headers=headers)
    exp = json.loads(res.text)['data']
    return exp

def coin(aid):
    data = {
        "aid": aid,
        "multiply": coinnumber,
        "select_like": select_like,
        "cross_domain": "true",
        "csrf": bili_jct
    }
    res = requests.post(url="https://api.bilibili.com/x/web-interface/coin/add", headers=headers, data=data)
    coinRes = json.loads(res.text)
    if coinRes['code'] == 0:
         print('投币成功')
    else:
        print('投币失败: 失败原因：' + coinRes['message'])

# 通知到微信
def sendmsgtowx(text='服务器挂掉啦~~',desp=''):
    if SCKEY == '':
        print('未配置推送微信')
        text = '未配置server酱'
        return
    else:
        url = "https://sc.ftqq.com/"+SCKEY+".send?text="+text+"&desp="+desp
        requests.get(url=url)

def sharevideo(aid):
    post_data = {
        "aid": aid,
        "csrf": bili_jct
        }
    res = requests.post(url="https://api.bilibili.com/x/web-interface/share/add", data=post_data,headers=headers)
    share_res = json.loads(res.text)
    if share_res['code'] == 0:
        print('视频分享成功')
    else:
        print('每日任务分享视频：' + share_res['message'])

    def silverToCoins(self):
        res1 = requests.get(url="https://api.live.bilibili.com/xlive/web-ucenter/user/get_user_info",headers=headers)
        silver_num = json.loads(res1.text)['data']['silver']
        if silver_num < 700:
            print('直播银瓜子不足700兑换硬币')
            return
        post_data = {
            "csrf_token": bili_jct,
            "csrf": bili_jct,
            # "visit_id": ""
        }
        res2 = requests.post(url="https://api.live.bilibili.com/pay/v1/Exchange/silver2coin",headers=headers, data=post_data)
        res_silver2Coins = json.loads(res2.text)
        if res_silver2Coins['code'] == 0:
            print('直播银瓜子兑换结果：成功')
        else:
            print('直播银瓜子兑换结果：'+res_silver2Coins['message'])

def report(aid, cid, progres):
    post_data = {
        "aid": aid,
        "cid": cid,
        "progres": progres,
        "csrf": bili_jct
        }
    res = requests.post(url="http://api.bilibili.com/x/v2/history/report", data=post_data,headers=headers)
    Res = json.loads(res.text)
    if Res['code'] == 0:
        print('上报视频进度成功')
    else:
        print('上报视频进度失败：' + Res['message'])

def checkTaskSituation():
    flag1 = flag2 = flag3 = False
    res = requests.get(url='https://account.bilibili.com/home/reward', headers=headers)
    if res.json()['data']['login'] == True:
        flag1 = True
    else:
        print("未得到登录经验")
    if res.json()['data']['coins_av'] == 50:
        flag2 = True
    else:
        print("未得到投币经验")
    if res.json()['data']['watch_av'] == True:
        flag3 = True
    else:
        print("未得到观看视频经验")
    return flag1 and flag2 and flag3
