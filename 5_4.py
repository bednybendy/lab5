n=int(input());org=n;fac=[];div=2
while div**2<=n:
    while n%div==0:
        fac.append(div)
        n//=div
    div+=1
if n>1:
    fac.append(n)
print(f'{org} = {' x '.join(map(str,fac))}')