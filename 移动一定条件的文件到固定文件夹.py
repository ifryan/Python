import os
import re
import shutil

# 定义文件源路径
source_path = "/Users/ryan/Documents/Ryan's Note"
destination_path = source_path + '/Assets'
file_endwith = '.md'

def raw_path(file):
    # 拼出文件全路径，后续检查是不是 dir 的时候需要用全路径
    return os.path.join(source_path,file)

def filted_by_OS(source_path,file_endwith):
    not_markdown = []
    # 列出所有文件,作为数组
    files = os.listdir(source_path)

    for file in files:

        # 等价于双层 if：
        # if not file.endswith(file_endwith):
        #    if not os.path.isdir(file_path):
        # 除文件夹和 md 文件之外 都会被加在数组中
        if not file.endswith(file_endwith) and not os.path.isdir(raw_path(file)):
            not_markdown.append(file)
    
    print(f'{len(not_markdown)} files\n')
    for item in not_markdown:
        print(item)
    
    return not_markdown

def filted_by_OS_and_Re(source_path,pattern):
    not_markdown = []
    for file in os.listdir(source_path):
    
        # 使用正则表达式匹配文件名
        if not pattern.match(file):
            # 检查是否是文件夹
            if not os.path.isdir(raw_path(file)):
                not_markdown.append(file)   
    
    print(f'{len(not_markdown)} files\n')
    for item in not_markdown:
        print(item)
    
    return not_markdown

def check_file_exist(file,path):
    # 检查文件在目录下是否存在，存在的话就改名
    for item in os.listdir(path):
        count = 1
        is_exist = True
        while is_exist:
            if file == item:
                file_name, file_extension = os.path.splitext(os.path.basename(raw_path(file)))
                new_name = f"{file_name}_{count}{file_extension}"
                os.rename(raw_path(file),raw_path(new_name))
                count+=1
            else:
                is_exist = False
    return file

    # count = 1
    # while file in os.listdir(path):
    #     file_name, file_extension = os.path.splitext(os.path.basename(raw_path(file)))
    #     new_name = f"{file_name}_{count}{file_extension}"
    #     os.rename(raw_path(file), raw_path(new_name))
    #     count += 1
    
    # return f"{file_name}_{count}{file_extension}" if count > 1 else file



def move_list_files_to_path(file_list,destination_path):
    # 捕获异常
    try:
        for item in file_list:
            item = check_file_exist(item,destination_path)
            
            # 第一个参数需要是全路径，第二个参数是个文件夹路径
            # 说是会覆盖同名文件，但是我运行的时候会报错
            shutil.move(raw_path(item),destination_path)
        print(f'done! \n move {len(file_list)}items')
    except Exception as e:
        print(f'Error:{e}')


files_to_be_move = filted_by_OS(source_path,file_endwith)
move_list_files_to_path(files_to_be_move,destination_path)
# pattern = re.compile(fr".*{re.escape(file_endwith)}$")
# filted_by_OS_and_Re(source_path,pattern)

