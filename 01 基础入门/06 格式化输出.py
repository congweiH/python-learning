# 格式化输出：
        # 1. 使用占位符
        # 2. format

person = 'jack'
address = 'China'
phone = '110'
num = 5
# 字符串 + 字符串是对的，但是字符串 + int 是错的
print('订单人是：'+person+', 收货地址: '+address+', 联系方式：'+phone)

# 错的
# print('数量：' + num)

print('订单人是：%s, 收货地址是：%s,联系方式: %s, 商品数量：%s' % (person, address, phone,num))

# 占位符有 %s   %d    %f   , 使用和c语言类似

#######################################
name = '赵飞'
print('姓名是：' + name)

age = 18
# print('年龄是：' + age)   错的
print('年龄是：%s' % age)   # 底层其实是 str(age)

# 将int强制转化成str
print('年龄是：' + str(age))

# 整数最好%d
print('年龄是：%d' % age)

# 练习
movie = '大侦探'
ticket = 45.59

message='''
电影: %s
单价：%.1f
''' % (movie, ticket)

print(message)

# format
age = 2
s = '幼儿园'
message = '我今年{}岁了,已经上{}了'.format(age, s)
print(message)