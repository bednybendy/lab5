n=int(input())
a,b=0,1
print(f'{n}')
for i in range(n):
    print(a,end=' ')
    a,b=b,b+a
print()