n=int(input())
org=n;s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==org: print('+')
else: print('-',s)