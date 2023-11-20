import pandas as pd
import os

# 读取 CSV 文件
csv = pd.read_csv('/Users/ryan/Downloads/finance.csv')

# 查找项目在 CSV 文件中的索引
def findItem(item):
    indexNum = 0
    for i in csv[csv.columns[0]]:
        if item == i:
            return indexNum
        indexNum += 1
    return -1

# 获取月份信息
def month(item):
    rowIndex = findItem(item)
    if rowIndex != -1:
        return csv[csv.columns[1]][rowIndex]
    else:
        return None 

# 获取年份信息
def year(item):
    rowIndex = findItem(item)
    if rowIndex != -1:
        return csv[csv.columns[2]][rowIndex]
    else:
        return None

# 获取类别信息
def catalog(item):
    rowIndex = findItem(item)
    if rowIndex != -1:
        return csv[csv.columns[3]][rowIndex]
    else:
        return None

# 获取其他信息
def others(item):
    rowIndex = findItem(item)
    if rowIndex != -1:
        return csv[csv.columns[4]][rowIndex]
    else:
        return None

# 批量修改文件内容
def batch_modify_content(folder_path):
    # 遍历文件夹
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(month(filename))
            new_str = f'---\n月金额: {month(filename)} \n年金额: {year(filename)}\n类别: {catalog(filename)}\nDate_created:\nLast_modified:\n---\n备注:: {others(filename)}'

            # 将修改后的内容写回文件
            with open(file_path, 'w') as file:
                file.write(new_str)

            print(f'文件 {filename} 已修改。')

# 批量创建文件
def batch_create(folder_path):
    for filename in csv[csv.columns[0]]:
        file_path = os.path.join(folder_path, f'{filename}.md')
        new_str = f'---\n月金额: {month(filename)} \n年金额: {year(filename)}\n类别: {catalog(filename)}\nDate_created:\nLast_modified:\n---\n备注:: {others(filename)}'
        
        with open(file_path,'w') as file:
            file.write(new_str)
        
        print(f'[[Dataview/个人财务管理/{filename}]]')

# 主程序
folder_path = '/Users/ryan/Documents/Ryan\'s Note/Dataview/个人财务管理'

# 调用批量创建文件的函数
batch_create(folder_path)
