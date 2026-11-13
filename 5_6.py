n=int(input())
org=n; r_n=0; t=n
while t>0:
    d=t%10
    r_n=r_n*10+d
    t//=10
if org==r_n: print(f'{org} палиндром ')
else: print(f'{org} не палиндром ')