# 接收用户输入的一行字符
string = input()
# 初始化各类字符计数器
letter = 0
digit = 0
space = 0
other = 0
# 遍历每个字符进行类型判断和计数
for char in string:
    if char.isalpha():
        letter += 1
    elif char.isdigit():
        digit += 1
    elif char.isspace():
        space += 1
    else:
        other += 1
# 按要求格式输出结果
print(f"英文字符: {letter}")
print(f"数字: {digit}")
print(f"空格: {space}")
print(f"其他字符: {other}")
