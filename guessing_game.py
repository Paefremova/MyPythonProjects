from random import *

def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100

num = randint(1,100)
print('Добро пожаловать в числовую угадайку')

while True:
    answ = input("Введите вашу догадку (число от 1 до 100): ")
    if not is_valid(answ):
        print("Ошибка, проверьте, что вы вводите число от 1 до 100")
        continue
    
    answ = int(answ)
    
    if answ > num:
        print("Слишком много, попробуйте еще раз")
    elif answ < num:
        print("Слишком мало, попробуйте еще раз")
    else:
        print("Вы угадали, поздравляем!")
        break