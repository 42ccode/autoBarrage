# bilibili直播发送弹幕
import requests
import random
import time

while True:
    time.sleep(random.randint(1,3))  #随机延迟
    lis = ["666", "主播牛逼", "主播真帅", "我爱主播","主播好厉害呀"] #自动发送组可自定义
    word = random.choice(lis)
    url = 'https://api.live.bilibili.com/msg/send'  #在发送弹幕后network url中获取
    data = {
        "bubble": "0",
        "msg": word,
        "color": "16777215",  #色号
        "mode": "1",
        "fontsize": "25",
        "room_type": "0",
        "rnd": "主播的rnd",  # 这里用network 然后抓包 筛选send 找pyload替换
        "roomid": "主播的房间id",  # 这里用network 然后抓包send 找pyload替换
        "csrf": "your_csrf",  #在payload中下方替换成你自己的
        "csrf_token": "your_scrf_token" #在payload中下方替换成你自己的
    }
    headers = {
        "Cookie": "your_cookie",
        "User-Agent": "your_user-agent"
    }

    response = requests.post(url=url, headers=headers, data=data)
    print(response.status_code)
