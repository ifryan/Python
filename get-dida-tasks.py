import requests
import json

url = "https://api.dida365.com/api/v2/batch/check/0"

headers = {
    "Host": "api.dida365.com",
    "Accept": "application/json, text/plain, */*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh,en-US;q=0.9,en;q=0.8,zh-CN;q=0.7",
    "Cache-Control": "no-cache",
    "Cookie": "t=43A001113F9610FF4B5DDB86647AD57594A56CFA422D97C2D41E34F6D6FD3DD7A889539CC2EDA5BE4FC2D8F8A4A67913268F76A0D4A72F7B86250A4FC33B7356AEE7490C6191291D296ADF924DEA641AE629C5F7AE5B67A8329A262AFFD886A91B6C15CC826D377B34DAE6D0D45553D2151002FFD8A51141F5935B9A8C9ED0F2306478F9DA33AB2DBB041D9EB60AD06F27C6E6AC6E0A5D8B5D8EAD2F3D42B85951CCFE3C193B95134C4FFBD3D1FB387E; SESSION=NTRkN2MyZWYtNjQwNy00YzlkLTk2N2MtNGM0YTU4MDQyMDAw; AWSALB=erOMd5kqiX8DWHB8Y8ZXzwo5ONO2v1XXNWj3R5LhgX8+jeXH7OMJuvZaV8L47pHAXA2cNVRClADpZf6GSRkSoI13q6kAxo7QVv2K8btFg03+RABUDVEco43Ppq2ujcZwDczhx88Ajxh0ynOgTz3xSozY9qGCggHt8YiostW0L7ISjCUXbU/bipTh720j3Q==; AWSALBCORS=erOMd5kqiX8DWHB8Y8ZXzwo5ONO2v1XXNWj3R5LhgX8+jeXH7OMJuvZaV8L47pHAXA2cNVRClADpZf6GSRkSoI13q6kAxo7QVv2K8btFg03+RABUDVEco43Ppq2ujcZwDczhx88Ajxh0ynOgTz3xSozY9qGCggHt8YiostW0L7ISjCUXbU/bipTh720j3Q==",
    "Dnt": "1",
    "Hl": "zh_CN",
    "Origin": "https://dida365.com",
    "Pragma": "no-cache",
    "Referer": "https://dida365.com/",
    "Sec-Ch-Ua": "\"Not=A?Brand\";v=\"99\", \"Chromium\";v=\"118\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"macOS\"",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-site",
    # "Traceid": "65360c9330b80127f26f2d48",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "X-Device": "{\"platform\":\"web\",\"os\":\"macOS 10.15.7\",\"device\":\"Chrome 118.0.0.0\",\"name\":\"\",\"version\":4585,\"id\":\"64c8b87a457fa853f3a796e2\",\"channel\":\"website\",\"campaign\":\"\",\"websocket\":\"65360c9030b80127f26f2d02\"}",
    "X-Tz": "Asia/Shanghai"
}

response = requests.get(url, headers=headers)

print(response.text)

# 写入文件
with open('response.txt', 'w') as f:
  f.write(response.text)
  
# 解析 JSON 响应文本
data = json.loads(response.text)

update_data = data.get("syncTaskBean", {}).get("update", [])

# 初始化空字典来存储数据
titles = {}
content = {}
startDates = {}
dueDates = {}

# 循环遍历更新数据
for i, task in enumerate(update_data):
    titles[i] = task.get("title")
    startDates[i] = task.get("startDate")
    dueDates[i] = task.get("dueDate")
    content[i] = task.get("content")

# # 打印任务列表
# for i in range(len(titles)):
#     task_info = f"- [ ] {titles[i]} - {startDates[i]} - {dueDates[i]}"
#     print(task_info)
    
# 创建一个文本文件来存储任务列表
with open('task_list.txt', 'w') as file:
    # 写入任务列表
    for i in range(len(titles)):
        task_info = f"- [ ] {titles[i]} - {startDates[i]} - {dueDates[i]}\n\t{content[i]}\n\n"
        file.write(task_info)

# 输出成功消息
print("任务列表已写入 task_list.txt 文件。")