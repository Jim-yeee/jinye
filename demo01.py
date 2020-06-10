'''
print('hello world') #字符串 str
print(100)    #整型  int
print(3.14)   #浮点型  float
print(True)   #布尔值  bool
print(())     #元组   tuple
print([])     #数组  list
print({})     #字典  dic

print("你好呀","我是美美")
print("嘻嘻"+"哈哈")
print("哈哈"*10)
print((1+2)*10+50)
print(1+1==3)   '''


#input输入
'''a=input("请输入你的名字：")
print("你的名字是：",a)'''

# print(type("嘻嘻"))
# print(type(100))
# print(type(3.14))
# print(type(True))
# print(type(()))
# print(type([]))
# print(type({}))


'''a=float(input("请输入数字："))
b=float(input("请输入数字："))
print("得出结果为：",a+b)'''


#len 获取字符串长度 （支持字符串、元组、数组、字典）
'''a="sdfjsagdsdfgasjgfjskfjksaggasjk"
print(len(a))'''


#练习：通过代码获取两段内容，并且计算他们的长度之和
a="我是第一段内容"
b="我是第二段内容"
print("他们的长度之和为：",len(a+b))