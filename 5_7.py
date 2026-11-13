n=int(input())

print('прямоугольник')
print()
for i in range(n): print('*'*n)
print()

print('треугольник')
for i in range(1,n+1): print('*'*i)
print()

print('елочка')
for i in range(1,n+1): print(' '*(n-i)+'*'*(2*i-1))
print()
print('ромб')
for i in range(1,n+1): print(' '*(n-i)+'*'*(2*i-1))
for i in range(n-1,0,-1): print(' '*(n-i)+'*'*(2*i-1))