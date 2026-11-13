n=int(input())
sum=0;p=1;sum_q=0
for i in range(1,n+1):
    sum+=i; p*=i; sum_q+=i**2
print(f'сумма {sum}');print(f'произведение {p}');print(f'сумма квадратов {sum_q}')