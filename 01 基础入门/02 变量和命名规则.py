"""
    1. 变量类型：
        字符串
        整数
        浮点数
        布尔类型： 只有True和False两个值
        
        列表list
        字典dict
        集合set
    
    2. python弱类型：变量里面的内容的类型可以更改，赋什么值就什么类型
        a = 1
        a = "hello"

        print(a, type(a))  # type(xxx) 返回变量xxx的类型

    3. 变量命名规范：
        1）由数字、字母和下划线（_）组成，不能以数字开头
        2）严格区分大小写
        3）不能使用关键字
            查看python有哪些关键字：
                import keyword
                print(keyword.kwlist)
        建议：
            1）驼峰式命名  getName
            2）类名每个单词首字母大写
            3）下划线式命名：get_name ~ getName。在python中推荐用，限于变量名和函数名。
"""

a = 'hello world'
print(a)