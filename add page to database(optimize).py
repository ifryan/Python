import requests
import json
import re

# 固定配置
NOTION_API_URL = "https://api.notion.com/v1/pages/"
BOT_SECRET_KEY = "secret_3vddc25OHXfAXdeRwercnG3dpYmvyhdcF2PC7Uk7yUy"

# 定义函数：发送 GET 请求获取页面 JSON
def get_page_info(page_url, headers=None):
    if headers is None:
        headers = {
            "Authorization": "Bearer " + BOT_SECRET_KEY,
            "Notion-Version": "2021-05-13"
        }

    # 提取页面ID
    page_id = re.findall(r"([a-zA-Z0-9]{32})", page_url)[0]

    response = requests.get(NOTION_API_URL + page_id, headers=headers)
    return response.json()

# 定义函数：发送 POST 请求以更新页面信息
def update_page_info(page_data, headers=None):
    if headers is None:
        headers = {
            "Authorization": "Bearer " + BOT_SECRET_KEY,
            "Notion-Version": "2021-05-13"
        }

    response = requests.post(NOTION_API_URL, json=page_data, headers=headers)
    return response.text

# 获取页面信息
notion_url = "https://www.notion.so/web3player/test-page-d2ef6a01fd8e4c7391d0a45a06b424a0?pvs=4"
page_info = get_page_info(notion_url)

# 输入要更改的标题
new_title = input("Enter the new title: ")

# 更新页面信息
page_info["properties"]["Name"]["title"][0]["text"]["content"] = new_title
page_info["properties"]["Name"]["title"][0]["plain_text"] = new_title

# 发送更新请求
response = update_page_info(page_info)

# 打印响应
print("Update Response:", response)
