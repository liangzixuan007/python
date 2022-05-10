import random
a=random.randint(1,100)
while True:
    b=input("请输入1到100之间的整数:")
    b=int(b)
    if(a==b):
        print("猜对了！")
        break
    elif(a>b):
        print("小了！")
    else:
        print("大了！")
