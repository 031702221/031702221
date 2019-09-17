import re

# 去除长注释，/*.....*/
long_comment = re.compile(r'/\* .*? \*/')
# 去除短注释，//..
short_comment = re.compile(r'//([^\n]*)')
short_comment1= re.compile(r'#([^\n]*)')
# 去除花括号 {...}
bracket = re.compile(r'[{}]')

code1_path = "./test_code/测试题/A0.c++.txt"
# 空白符匹配正则
bracket_pattern = re.compile(r'[ \t]+')

# 指针变量匹配
pointer = re.compile(r'\*+[ \f\r\t\v]+[\w]+')

# 去除注释
def remove_comment(code):
    # 去除短注释，//..
    code = short_comment.sub('',code)
    code = short_comment1.sub('',code)
    # 去除长注释，/*.....*/
    code = long_comment.sub('',code)

    # 去除花括号 {...}
    code = bracket.sub('',code)

    pointer_vars = pointer.findall(code)
    for var in pointer_vars:
        blank_re = re.compile(r'[\s]+')
        new_var = blank_re.sub('',var)
        code = code.replace(var,' '+new_var)
    # print(code)
    return code
#with open(code1_path,'r') as test1:
#    code = test1.read()
#print(remove_comment(code))

# 去除花括号
def remove_bracket(code):
    code = bracket_pattern.sub('',code)
    code_lines = code.split('\n')
    # print(code)
    # print(code_lines)
    new_code = []
    for line in code_lines:
        if line != '':new_code.append(line)
    return new_code

#-------------public------------------------------

# 代码格式化
def format_code_main(code):
#    code = remove_comment(code)
    return remove_bracket(code)

# 代码分割
def code_slicing(code:list,step:int):
    new_code=[]
    length = len(code)
    for idx in range(0,length,step):
        new_code.append(code[idx:idx+step])
    # new_code.append(code[idx:])

    return new_code
