import requests
import json
import datetime

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

# 解析 JSON 响应文本
data = json.loads(response.text)

# Extract new data from the response
new_data = data.get("syncTaskBean", {}).get("update", [])

def add_tab_to_lines(input_text):
    lines = input_text.split('\n')  # 按换行符分割文本成行
    indented_lines = ['\t' + line for line in lines]  # 在每行前面加上制表符
    indented_text = '\n'.join(indented_lines)  # 重新组合成文本
    return indented_text

def convert_time_format(type,time):
    if type == "start":
      emoji = f"📅"
    else :
      emoji = f"🛫"
    time_str = str(time)
    if time_str == "None":
      return None
    else : 
      dt = datetime.datetime.fromisoformat(time_str.replace('Z', '+00:00'))
      return f"{emoji} {dt.year}-{dt.month}-{dt.day}"    

try:
    with open('response_json', 'r', encoding="utf-8") as f:
        old_data = json.load(f)
except FileNotFoundError:
    old_data = {"syncTaskBean": {"update": []}}

num = 0
# Find deleted items by comparing old and new data
# print(old_data["syncTaskBean"]["update"][0]["content"])
deleted_items = [item for item in old_data["syncTaskBean"]["update"] if item not in new_data]

# If there are deleted items, append them to a file
if deleted_items:
    with open('Done_list', 'a', encoding="utf-8") as f:
        for item in deleted_items:
            num += 1
            if "content" not in item:
                item["content"]=""        
            f.write(f'- [x] {item["title"]} #task {convert_time_format("start", item["startDate"])} {convert_time_format("due", item["dueDate"])}\n {add_tab_to_lines(item["content"])} \n')

# Update the old data with the new data
old_data["syncTaskBean"]["update"] = new_data

# Save the updated data to the file
with open('response_json', 'w', encoding="utf-8") as f:
    json.dump(old_data, f, ensure_ascii=False)

print(str(len(new_data)) + " to do created\n" + str(num) + " done created")
