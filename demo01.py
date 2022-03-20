"""
print('hello world')  #  字符串 单行注释
print(2333)    # 整数/str
print(2.33)   #小数/float
print(((1+2.2)*50-9.9)/2)  #python中都是小括号
print(True)   # 布尔值/bool
print(2>3)
print(())  # 元组/tuple
print([])  # 数组/list
print({})  # 字典/dict
#空 NoneType
"""
"""
多行注释的内容
"""
"""
print('哈哈哈',2333,9.8,(),[],{}) #同时打印多个内容
print('今天'+'好冷啊') #同类型可直接拼接，字符串只能用+号无-号
print('你好'*5) # *号表示字符串多少个,*5表示打印出5个你好

运算符号：+ - * / %（余）
逻辑符号:and和not and, or和not or, =和!=

name='张三' # 变量/赋值。将张三这个值赋值给变量name,print之后的就是变量的值了
print(name)

a = input("请输入:") # input中只能输入字符串类型
print('input获取的内容:',a) #保存之后执行python demo01.py,然后输入内容就可以打印出来了

# c = type(988.6) #type可以进行数据格式的转换，float为浮点型
# input(c)   Ctrl+?快捷键 - 快速注释
d=int(2.33)
print(type(d))

a=float(input("请输入："))
b=float(input("请输入："))
print("input获取的内容:",a+b)
"""
#练习:通过代码获取两段内容，并且计算他们的长度的和
a=input("请输入:")  #空格也算一个字符
b=input("请输入:")
print("两端字符串的长度是:",len(a)+len(b))