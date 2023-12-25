def deduplication(list):
    temp = []
    for item in list:
        if item not in temp:
            temp.append(item)
    return temp

dictList = []
# lines = rawtext.splitlines()

with open('temp','r') as f:
    for line in f.readlines():
        # strip 方法可以去掉开头的空格和换行符
        for char in line.strip():
            dictList.append(char)

print('before: length:'+str(len(dictList))+str(dictList))

# new_list=deduplication(dictlist)

# sorted函数不会修改原 list，会返回结果
newList = sorted(list(set(dictList)))

# sort方法会修改原 list，并且返回 none
# newList = list(set(dictList))
# newList.sort()

def diffList(raw,unique):
    for i in unique:
        if i in raw:
            raw.remove(i)
    return raw

diffList = diffList(dictList,newList)
print(f'length:{len(diffList)},{diffList}')


with open('temp','w') as f:
    for i in newList:
        f.write(f'{i}')