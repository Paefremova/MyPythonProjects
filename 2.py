n = int(input())
answ = ''
while n != 0:
    num = n % 2
    n = n // 2
    answ = str(num) + answ
print(answ)