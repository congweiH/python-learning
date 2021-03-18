# 1. 打印常量
print('hello world')
print(3)
# 2. 打印变量
name = '小明'
print(name)

# 3. print(name, age, gener)  分隔符默认： 空格，
        # print(value,...,sep=' ',end='\n',file=sys.stdout,flush=False)
age = 18
gender = '男'
print(name, age, gender)    # 小明 18 男


# 4. 更改分隔符sep
print(name, age, gender, sep='-')    # 小明-18-男

# 5. 更改结尾end， 默认 end='\n'换行
print('aaa',end='')     # 取消结尾换行  'aaa\n'   ->  'aaa'
print('bbb',end='')     #               'bbb\n'  ->  'bbb'                  
print('ccc',end='')     # aaabbbccc     'ccc\n'  ->  'ccc'

"""
    练习: 
        用一个print输出：
            亲爱的xxx:
                    请点击链接激活用户：激活用户
"""
print('\n亲爱的xxx:\n    请点击链接激活用户：激活用户')