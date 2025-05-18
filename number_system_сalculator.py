
bin_str = input("Введите шестнадцатеричное число: ")

decimal_value = 0 
power = 0  

for i in range(len(bin_str) - 1, -1, -1):
    if bin_str[i].isalpha():
        bit = ord(bin_str[i].upper()) - 55
    else:    
        bit = int(bin_str[i])
    decimal_value += bit * (16 ** power) 
    power += 1  

print("Десятичное число:", decimal_value)

