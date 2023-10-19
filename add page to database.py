import requests
import json
import re

# 固定配置
url = "https://api.notion.com/v1/pages/"

# 机器人 secret key
token = "secret_3vddc25OHXfAXdeRwercnG3dpYmvyhdcF2PC7Uk7yUy"

# 想要新增 page 的数据库同级 page
notionurl = "https://www.notion.so/web3player/test-page-d2ef6a01fd8e4c7391d0a45a06b424a0?pvs=4"

# 通过正则表达式把链接中的连续 32 位英文或数字摘取出来，注意取出后是数组，所以要用[0]来取出数据
pageid = re.findall(r"([a-zA-Z0-9]{32})",notionurl)[0]

# 定义函数
# 请求get 获取页面json
def getInfo(pageid):
    resp = requests.request(
        #第一个参数，request 方式，
        "GET", 

        #第二个参数，请求地址，string
        url + pageid ,

        # 固定 headers，token 是机器人 key
        headers={
            "Authorization": "Bearer " + token,
            "Notion-Version": "2021-05-13"
            }, 
            )
    #返回请求回传参数（**字符串**）
    return resp.text

# 定义函数
# 发送post 新增请求
def postInfo(update_pagebody):
    resp = requests.request(
        "POST", 

        #第二个参数，请求地址，string，这里是固定值，此处定位主要由 get 的 json 中的 id 来定位
        url,

        #请求body
        json = update_pagebody, 

        #请求 headers 固定
        headers={
            "Authorization": "Bearer " + token,
            "Notion-Version": "2021-05-13"
            },
            )
    #返回请求回传参数（**字符串**）
    return resp.text

# getinfo 函数得到的是 json 样式的字符串，需要用 json.loads 读成 json 文件
# 读成 json 文件才可以用数组下标的形式读数据
# update_pagebody =json.dumps(pagebody,indent=4)
# 这个方法可以把 json 变回字符串，indent=4 表示缩进用的空格数
pagebody = json.loads(getInfo(pageid))

# 输入想要的标题
changetitle = input("title")

# 修改 json 中的值，{}大括号包裹的需要用["属性名"]来索引，[]中括号包裹的需要用[下标]来索引
pagebody["properties"]["Name"]["title"][0]["text"]["content"] = changetitle
pagebody["properties"]["Name"]["title"][0]["plain_text"] = changetitle

# 组合打印需要用这样的形式
# print("update_pagebody: " + update_pagebody)
# 此处 pagebody 是 json 格式，所以可以直接做参数传入
print(postInfo(pagebody))




