a=input("a:")
b=input("b:")
a=int(a)
b=int(b)
s1=a+b
s2=a-b
s3=a*b
s4=round(a/b)
s5=a*a+b*b
s6=a*a
s7=b*b
s8=a*a*a
s9=b*b*b
print("相加:",s1)
print("相减:",s2)
print("相乘:",s3)
print("相除:",s4)
print("平方相加:",s5)
print("a的平方：",s6)
print("b的平方：",s7)
print("a的立方:",s8)
print("b的立方:",s9)
if a>b:
    print("a>b",a)
elif a == b:
    print("a = b")
else:
    print("a < b",b)
