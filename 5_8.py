try:
    n=int(input())
    org=n;s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==org: print('совершенное')
    else: print('не совершенное, кол-во',s)
except ValueError: print('не число ')