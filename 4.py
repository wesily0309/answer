a=int(input())
b=int(input())
c=int(input())
cc=b**2-(4*a*c)

if cc==0:
    x=(-cc)/(2*a)
    print(x)
elif cc>0:
    x=((-b)+((b**2)-(4*a*c)))/2*a
    y=((-b)-((b**2)-(4*a*c)))/2*a
    print(x,y)
else:
    print("Your equation has no root.")