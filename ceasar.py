print("Привет, дорогой пользователь. Я помогу тебе сгенерировать шифр Цезаря!")
k = int(input('Введите шаг сдвига: '))

en_upper = [chr(i) for i in range(65, 91)]   
en_lower = [chr(i) for i in range(97, 123)]  

ru_upper = [chr(i) for i in range(1040, 1072)]  
ru_lower = [chr(i) for i in range(1072, 1104)]  

def cezar(text):
    if text[0] in en_upper + en_lower:
        upper = en_upper
        lower = en_lower
        length = 26
    else:
        upper = ru_upper
        lower = ru_lower
        length = 32

    for char in text:
        if char in upper:
            c = upper.index(char)
            new_c = (c + k) % length
            print(upper[new_c], end='')
        elif char in lower:
            c = lower.index(char)
            new_c = (c + k) % length
            print(lower[new_c], end='')
        else:
            print(char, end='')

txt = input('Введите текст: ')
cezar(txt)
