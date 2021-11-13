from fun import *
import random


if __name__ == '__main__':
    user = User()          #基本信息
    liveSign()              #直播签到
    comicSign()             #漫画签到
    hotvideolist = getHotVideo()
    sharevideo(aid=hotvideolist[random.randint(1, 50)]['aid'])      #分享视频
    slivertocoin()
    a = random.randint(1, 50)
    report(hotvideolist[a]['aid'], hotvideolist[a]['cid'], 1000)    #观看视频
    for item in hotvideolist:  #投币
        if getCoinTodayExp() == 50:
            print(('投币任务已完成，已获得所有投币经验'))
            break
        coin(item['aid'])
    desp = f'你的当前等级是{user.currentlevel}, 当前经验为{user.current_exp}, 离下一级还有{user.current_min}, 下一级还需{user.next_exp - user.current_exp}经验, \
    还有{int((user.next_exp - user.current_exp)/65)}天升级 ,B币余额为{user.bcoin_balance}'
    if int(user.bcoin_balance) >= 5:
        charge(int(user.mid))
    if checkTaskSituation():
        sendmsgtowx(f'今日哔哩哔哩任务已完成，还有{int((user.next_exp - user.current_exp)/65)}天升级', desp)

