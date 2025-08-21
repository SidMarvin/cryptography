"""
необходимо добавить условие, когда переменная ciphersymbol_number (это индекс буквы шифртекста) превышает длину алфавита, ибо мы получаем ошибку IndexError: string index out of range 
"""



alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphavite_eng = "abcdefghijklmnopqrstuvwxyz"

mod = input("Выбран шифр Виженера. Выберите действие:\n[1] Зашифровать\n[2] Расшифровать\n:  ")

if mod == "1" or mod == "e":
    text_lang = input("Выберите язык для зашифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        print("Выбран русский язык.")
        open_text = input("Введите текст для зашифровки: ")
        input_key = input("Введите ключ: ")
        close_text = ""
        #проверка на символы (должны быть только буквы)
        #проверка что ключ не длиннее текста
        lenght_key = len(input_key) #длина ключа
        
        len_ot = len(open_text)
        len_it = len(input_key)
        
        #если длина текста больше длины ключа
        if len_ot > len_it: 
            #если длина текста кратна длине ключа
            if len_ot % len_it == 0:
                delta = len(open_text) // len(input_key)
                input_key = input_key * delta

                #шифрование
                for i, j in zip(open_text.lower(), input_key.lower()):
                    if i in alphavite_rus:
                        number_open_text = alphavite_rus.index(i) #индекс буквы открытого текста
                        number_key = alphavite_rus.index(j) #индекс буквы ibahntrcnf текста
                        ciphersymbol_number = number_open_text + number_key #индекс зашифрованной буквы
                        close_text += (alphavite_rus[ciphersymbol_number]) 
                    else:
                        pass
                        
            #если длина текста НЕ кратна длине ключа            
            elif len_ot % len_it != 0:
                delta = len(open_text) // len(input_key)
                input_key = input_key * delta + input_key[:(len(open_text) % len(input_key))]
                #шифрование
                for i, j in zip(open_text.lower(), input_key.lower()):
                    if i in alphavite_rus:
                        number_open_text = alphavite_rus.index(i) #индекс буквы открытого текста
                        number_key = alphavite_rus.index(j) #индекс буквы ключа
                        ciphersymbol_number = number_open_text + number_key #индекс зашифрованной буквы
                        close_text += (alphavite_rus[ciphersymbol_number])

        #если длина текста меньше длины ключа
        elif len_ot < len_it: 
            input_key = input_key[:len(open_text)]
            #шифрование
            for i, j in zip(open_text.lower(), input_key.lower()):
                if i in alphavite_rus:
                    number_open_text = alphavite_rus.index(i) #индекс буквы открытого текста
                    number_key = alphavite_rus.index(j) #индекс буквы ibahntrcnf текста
                    ciphersymbol_number = number_open_text + number_key #индекс зашифрованной буквы
                    close_text += (alphavite_rus[ciphersymbol_number]) 
            
        #если длина текста равна длине ключа
        elif len_ot == len_it: 
            #шифрование
            for i, j in zip(open_text.lower(), input_key.lower()):
                if i in alphavite_rus:
                    number_open_text = alphavite_rus.index(i) #индекс буквы открытого текста
                    number_key = alphavite_rus.index(j) #индекс буквы ibahntrcnf текста
                    ciphersymbol_number = number_open_text + number_key #индекс зашифрованной буквы
                    close_text += (alphavite_rus[ciphersymbol_number]) 
            
        print(close_text)       

                       
    
elif mod == "2" or mod == "d":
    text_lang = input("Выберите язык для расшифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        decode_mod = input("Выбран русский язык. Что нужно сделать? \n[Тест Казиски] \n[Атака по словарю] \n[Умный брутфорс]")
        if decode_mod == "1":
            None
            


 
#написать тест Касиски
#атаковать по словарю
#атаковать брутфорсом на манер шифра Цезаря, но применять частоный анализ для рассчета появления букв
