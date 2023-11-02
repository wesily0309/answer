a=int(input('筆數'))
b=[]
for i in range(a):
    e=input('xxx(銷貨填負) xxx:').split(' ')
    b.append(list(map(int,e)))
#[數量,價格]
c=0
r=0
for i in range(len(b)):
    if b[i][0]<0:
        f=0
        for d in range(abs(b[i][0])):
            if b[f][0]<=0:
                f+=1
            c+=b[f][1]
            r+=b[i][1]
            b[f][0]-=1
            if b[f][0]==0:
                f+=1
            if b[f][0]<0:
                break
        b[i][0]=0
print(f'銷貨成本:{c}')
print(f'毛利:{r-c}')
