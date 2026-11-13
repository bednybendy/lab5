n=int(input())
c=0;t=0;p=0;r_n=0;org=n
while n>0:
    d=n%10;c+=1;t+=d;p*=d;r_n=r_n*10+d;n//=10
print(f'{c}');print(f'{t}');print(f'{p}');print(f'{r_n}')