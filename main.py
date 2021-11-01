import requests

from fun import *
import random


if __name__ == '__main__':
    getuserInfo()
    liveSign()
    comicSign()
    hotvideolist = getHotVideo()
    sharevideo(aid=hotvideolist[random.randint(1, 50)]['aid'])
    a = random.randint(1,50)
    report(hotvideolist[a]['aid'],hotvideolist[a]['cid'],1000)
    for item in hotvideolist:  #50经验
        if getCoinTodayExp() == 50:
            print(('投币任务已完成，已获得所有投币经验'))
            break
        coin(item['aid'])
    if checkTaskSituation():
        sendmsgtowx('今日任务已完成，程序结束,')

