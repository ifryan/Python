# obtain = False
# num_line=[]

# for i in range(0,20008):
#     for num in str(i):
#         if num == '8':
#             obtain = True
#             break
#     if obtain:
#         num_line.append(i)
#     obtain = False

number = input('Please input the number : ')

num_line = [i for i in range(int(number)+1) if any(digit == '8' for digit in str(i))]

print(f"共有 {len(num_line)} 个数字有中存在 8 ,分别是:")
for i in num_line:
    print(f'{i}',end='\n')