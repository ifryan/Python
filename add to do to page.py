import requests
import json
import re

# 获取页面信息
notion_url = "https://www.notion.so/web3player/test-page-d2ef6a01fd8e4c7391d0a45a06b424a0?pvs=4"
page_info = get_page_info(notion_url)

# 输入要创建的To-Do标题
todo_content = "input"

# 创建To-Do数据
todo_data = {
    "object": "block",
    "id": "c02fc1d3-db8b-45c5-a222-27595b15aea7",
    "type": "to_do",
    "parent": {
	    "type": "block_id",     
        "block_id": page_info["id"]
    },
    "to_do": {
        "rich_text": [
            {
                "type": "text",
                "text": {
                    "content": todo_content
                }
            }
        ]
    }
}

# 创建To-Do
todo_response = create_todo(page_info["id"], todo_data)

# 获取To-Do的URL
print(todo_response['message'])
# todo_url = todo_response.get("url", "URL字段不存在")
# print("To-Do URL:", todo_url)
