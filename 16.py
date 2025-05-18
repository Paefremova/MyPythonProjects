n = int(input())
answ = ""
while n != 0:
    ost = n % 16
    if 9 < ost < 16:
        ost = chr(ost+55)
    n = n // 16
    answ = str(ost) + answ
print(answ)