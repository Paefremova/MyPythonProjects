import random

def generate_password(length, chars):
    password = '' 
    for i in range(length):
        password += random.choice(chars)
    return password

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''
count = 0

print("Привет, дорогой пользователь. Я помогу тебе сгенерировать пароли!\nВ них будет как минимум по одному элементу из тех, какие тебе нужны! ")

k = int(input("Введите желаемое количество сгенерированных паролей!\n"))
dig = input('Включать ли цифры 0123456789? (да/нет)\n')
ABC= input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (да/нет)\n')
abc = input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (да/нет)\n')
ch = input('Включать ли символы !#$%&*+-=?@^_? (да/нет)\n')
strange = input('Исключать ли неоднозначные символы il1Lo0O? (да/нет)\n')

if dig.lower() == 'да':
    chars += digits
    count += 1
if ABC.lower() == 'да':
    chars += uppercase_letters
    count += 1
if abc.lower() == 'да':
    chars += lowercase_letters
    count += 1
if ch.lower() == 'да':
    chars += punctuation
    count += 1
if strange.lower() == 'да':
    for c in 'il1Lo0O':
        chars = chars.replace(c, '')

if not chars:
    print("Как так! - ни один тип символов не выбран для генерации пароля(.")
else:
    print("\nСгенерированные пароли почти готовы! ")
    for i in range(count):
        len_pw = int(input(f"Введите длину для пароля номер {i+1}:\n"))
        while len_pw < count:
            len_pw = int(input(f"Длина пароля слишком мальенькая, мы не уместим необходимые вам символы из разных категорий, введите число >= {count}:\n"))
        print(f"Я твой пароль № {i+1}:")
        print(generate_password(len_pw, chars))
