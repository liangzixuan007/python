import random
while True:
    a=random.choice(("石头","剪刀","布"))
    b=input("石头,剪刀,布")
    print("电脑出：",a)
    print("你出：",b)
    if(a==b):
        print("平局！")
    elif(a=="石头"and b=="剪刀"):
        print("电脑赢！")
    elif(a=="石头"and b=="布"):
        print("电脑输！")
    elif(a=="剪刀"and b=="布"):
        print("电脑赢！")
    elif(a=="剪刀"and b=="石头"):
        print("电脑输！")
    elif(a=="布"and b=="石头"):
        print("电脑赢！")
    elif(a=="布"and b=="剪刀"):
        print("电脑输！")
    elif(b=="exit"):
        print("退出程序!")
        break

