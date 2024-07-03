README
Introduction 介绍
This Python script automates the sending of comments (barrages) in a Bilibili live stream. It randomly selects a message from a predefined list and sends it at random intervals.

这个Python脚本可以自动在Bilibili直播间发送弹幕。它会从预定义的消息列表中随机选择一条消息，并以随机间隔发送。

Requirements 需求
Python 3.x
requests library
You can install the requests library using the following command:

你可以使用以下命令安装requests库：

bash
复制代码
pip install requests
Usage 用法
Set Up the Script 配置脚本

Before running the script, you need to replace the placeholders with your own information:

在运行脚本之前，你需要将占位符替换为你自己的信息：

your_csrf and your_csrf_token: Your Bilibili CSRF token. Replace this with the actual token from your account.
你的Bilibili CSRF token。用你账户的实际token替换。
your_cookie: Your Bilibili cookie. Replace this with the actual cookie from your account.
你的Bilibili cookie。用你账户的实际cookie替换。
your_user-agent: Your browser's user-agent string. Replace this with your actual user-agent.
你的浏览器user-agent字符串。用你实际的user-agent替换。
主播的rnd: The random number from the broadcaster. Replace this with the actual random number captured from the network payload.
主播的rnd。用从网络抓包中获取的实际随机数替换。
主播的房间id: The broadcaster's room ID. Replace this with the actual room ID captured from the network payload.
主播的房间id。用从网络抓包中获取的实际房间id替换。
Run the Script 运行脚本

You can run the script using the following command:

你可以使用以下命令运行脚本：

bash
复制代码
python send_barrage.py
Code 代码
python
复制代码
import requests
import random
import time

while True:
    time.sleep(random.randint(1, 3))  # 随机延迟
    lis = ["666", "主播牛逼", "主播真帅", "我爱主播", "主播好厉害呀"]  # 自动发送组可自定义
    word = random.choice(lis)
    url = 'https://api.live.bilibili.com/msg/send'  # 在发送弹幕后network url中获取
    data = {
        "bubble": "0",
        "msg": word,
        "color": "16777215",  # 色号
        "mode": "1",
        "fontsize": "25",
        "room_type": "0",
        "rnd": "主播的rnd",  # 这里用network 然后抓包send 找pyload替换
        "roomid": "主播的房间id",  # 这里用network 然后抓包send 找pyload替换
        "csrf": "your_csrf",  # 在payload中下方替换成你自己的
        "csrf_token": "your_csrf_token"  # 在payload中下方替换成你自己的
    }
    headers = {
        "Cookie": "your_cookie",
        "User-Agent": "your_user-agent"
    }

    response = requests.post(url=url, headers=headers, data=data)
    print(response.status_code)
Notes 注意事项
Make sure to comply with Bilibili's terms of service when using this script.
使用此脚本时，请确保遵守Bilibili的服务条款。
The script uses random intervals to avoid being detected as spam.
脚本使用随机间隔以避免被检测为垃圾信息。
This script is for educational purposes only. Please use it responsibly.
此脚本仅供教育用途。请负责任地使用。
If there is any legal risk involved, you should bear all the costs, the author only provides for learning purposes
如涉及法律风险一切需您自行承担,作者只提供学习用途