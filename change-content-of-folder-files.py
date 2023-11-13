import os

def batch_modify_content(folder_path, new_str):
    # 遍历文件夹
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            with open(file_path, 'w') as file:
                file.write(new_str)

            print(f'文件 {filename} 已修改。')

# 使用示例
folder_path = '/Users/ryan/Documents/Ryan\'s Note/Dataview/个人财务管理'
new_str = '---\n月金额: \n年金额: \n类别: \nDate_created:\nLast_modified:\n---\n备注::'

batch_modify_content(folder_path, new_str)
