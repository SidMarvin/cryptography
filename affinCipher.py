import math
import sys

alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphavite_eng = "abcdefghijklmnopqrstuvwxyz"

mod = input("Выбран Аффинный шифр. Выберите действие:\n[1] Зашифровать\n[2] Расшифровать\n:  ")


if mod == "1" or mod == "e": #зашифрование
    encode_text = ""
    text_lang = input("Выберите язык для зашифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        text = input("Введите текст для зашифрования: ")
        m = len(alphavite_rus)
        #выбираем ключи
        a = int(input("Введите ключ а (число, взаимно простое с размером алфавита: 1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32): "))
        #проверка ключей
        if math.gcd(a, m) == 1:
            print("Ключ подобран верно")
        else:
            print(f"Число {a} не является взаимно простым с мощностью алфавита {m}")
            sys.exit("Завершение программы")
        
        b = int(input(f"Введите ключ b (сдвиг, который равен от 0 до размера алфавита {m} минус 1): "))
        if b <= m-1:
            print("Условия соблюдены верно")
        else: 
            print(f"Число {b} больше чем {m}")
            sys.exit("Завершение программы")
        
        #магия криптографии
        for i in text.lower():
            if i in alphavite_rus:
                x = alphavite_rus.index(i)
                crypt_symbol_index = (a*x + b)% m
                encode_text = encode_text + alphavite_rus[crypt_symbol_index]
            elif i not in alphavite_rus: 
                encode_text = encode_text + i 
                
        print(encode_text)
    
    elif text_lang == "2":
        text = input("Введите текст для зашифрования: ")
        m = len(alphavite_eng)
        #выбираем ключи
        a = int(input("Введите ключ а (число, взаимно простое с размером алфавита): "))
        #проверка ключей
        if math.gcd(a, m) == 1:
            print("Ключ подобран верно")
        else:
            print(f"Число {a} не является взаимно простым с {m}")
            sys.exit("Завершение программы")
        
        b = int(input("Введите ключ b (сдвиг, который равен от 0 до размера алфавита): "))
        if b <= m-1:
            print("Условия соблюдены верно")
        else: 
            print(f"Число {b} больше чем {m}")
            sys.exit("Завершение программы")
        
        #магия криптографии
        for i in text.lower():
            if i in alphavite_eng:
                x = alphavite_eng.index(i)
                crypt_symbol_index = (a*x + b)% m
                encode_text = encode_text + alphavite_eng[crypt_symbol_index]
            elif i not in alphavite_eng: 
                encode_text = encode_text + i 
                
        print(encode_text)

        
elif mod == "2" or mod == "в": #дешифровка
    #decode_text = ""
    decode_text_list = []
    text_lang = input("Выберите язык для расшифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        m = len(alphavite_rus)
        a_list = [1, 2, 4, 5, 7, 8, 10, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 28, 29, 31, 32] #список взаимно простых чисел с мощностью российского алфавита
        b_list = [i for i in range(m)]

        text = input("Введите текст для расшифрования: ")

        #магия криптографии
        for a in a_list:
            for x in range(1, m):
                if (a*x) % m == 1:
                    inv_a = x
            for b in b_list:
                decode_text = ""
                for i in text.lower():  
                    if i in alphavite_rus: 
                        y = alphavite_rus.index(i)
                        decrypt_symbol_index = inv_a * (y - b) % m #правило дешифровки
                        decode_letter = alphavite_rus[int(decrypt_symbol_index)]
                        decode_text += decode_letter 
                    else:
                        decode_text += i 
                        
                decode_text_list.append(f" {a}, {b}: {decode_text}")

    with open('output.txt', 'w') as file:
        for result in decode_text_list:
            file.write(f"{result}\n")
        print("Результаты сохранены в файле output.txt")

                                               

    #elif text_lang == "2":
        #text = input("Введите текст для расшифрования: ")"""
