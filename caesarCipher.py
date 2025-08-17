alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphavite_eng = "abcdefghijklmnopqrstuvwxyz"

mod = input("Выбран шифр Цезаря. Выберите действие:\n[1] Зашифровать\n[2] Расшифровать\n:  ")

if mod == "1" or mod == "e":
    encode_text = ""
    text_lang = input("Выберите язык для зашифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        text = input("Введите текст для зашифрования: ")
        key = int(input("Введите ключ: "))
        for i in text.lower():
            if i in alphavite_rus:
                number_t = alphavite_rus.index(i) + key #индекс буквы открытого текста
                if number_t >= len(alphavite_rus) - 1:
                    number_t = len(alphavite_rus) - number_t  #индекс буквы шифртекста
                    encode_letter = alphavite_rus[-number_t] #буква шифртекста
                    encode_text = encode_text + encode_letter #шифртекст
                else:    
                    encode_letter = alphavite_rus[number_t] #буква шифртекста
                    encode_text = encode_text + encode_letter #шифртекст
            elif i not in alphavite_rus:        
                encode_text = encode_text + i 
        print(encode_text)
        input()
        
    elif text_lang == "2":
        text = input("Введите текст для зашифрования: ")
        key = int(input("Введите ключ: "))
        for i in text.lower():
            if i in alphavite_eng:
                number_t = alphavite_eng.index(i) + key #индекс буквы открытого текста
                if number_t >= len(alphavite_eng) - 1:
                    number_t = len(alphavite_eng) - number_t  #индекс буквы шифртекста
                    encode_letter = alphavite_eng[-number_t] #буква шифртекста
                    encode_text = encode_text + encode_letter #шифртекст
                else:    
                    encode_letter = alphavite_eng[number_t] #буква шифртекста
                    encode_text = encode_text + encode_letter #шифртекст
            elif i not in alphavite_eng:        
                encode_text = encode_text + i 
        print(encode_text)
        input()
        
elif mod == "2" or mod == "d":
    text_lang = input("Выберите язык для расшифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        decode_mod = input("Выберите атаку: \n[1] Вручную (сами введете ключ) \n[2] Брутфорс ключей \n: ")
        if decode_mod == '1' or decode_mod == "m":
            decode_text = ""
            text = input("Введите текст для расшифровки: ")
            key = int(input("Введите ключ: "))
            for i in text.lower(): 
                if i in alphavite_rus:
                    number_t = alphavite_rus.index(i) - key #индекс буквы шифртекста
                    if number_t >= len(alphavite_rus) - 1:
                        number_t = len(alphavite_rus) - number_t  #индекс буквы шифртекста
                        decode_letter = alphavite_rus[-number_t] #буква шифртекста
                        decode_text = decode_text + decode_letter #шифртекст
                    else:    
                        decode_letter = alphavite_rus[number_t] #буква открытого текста
                        decode_text = decode_text + decode_letter #открытый текст
                elif i not in alphavite_rus:   
                    decode_text = decode_text + i
            print(decode_text)
            input()
        
        elif decode_mod == '2' or decode_mod == "bf":
            decode_text = ""
            text = input("Введите текст для расшифровки: ")
            key = range(1, (len(alphavite_rus)))
            for j in key:
                for i in text.lower(): 
                    if i in alphavite_rus:
                        number_t = alphavite_rus.index(i) + j #индекс буквы шифртекста
                        i.lower()
                        if number_t >= len(alphavite_rus) - 1:
                            number_t = len(alphavite_rus) - number_t  #индекс буквы шифртекста
                            decode_letter = alphavite_rus[-number_t] #буква шифртекста
                            decode_text = decode_text + decode_letter #шифртекст
                        else:    
                            decode_letter = alphavite_rus[number_t] #буква открытого текста
                            decode_text = decode_text + decode_letter #открытый текст
                    elif i not in alphavite_rus:   
                        decode_text = decode_text + i
                print("ROT" + str(j) + ": " + decode_text[-len(text):] + "\n")
                input()

    if text_lang == "2":
        decode_mod = input("Выберите атаку: \n[1] Вручную (сами введете ключ) \n[2] Брутфорс ключей \n: ")
        if decode_mod == '1' or decode_mod == "m":
            decode_text = ""
            text = input("Введите текст для расшифровки: ")
            key = int(input("Введите ключ: "))
            for i in text.lower(): 
                if i in alphavite_eng:
                    number_t = alphavite_eng.index(i) - key #индекс буквы шифртекста
                    if number_t >= len(alphavite_eng) - 1:
                        number_t = len(alphavite_eng) - number_t  #индекс буквы шифртекста
                        decode_letter = alphavite_eng[-number_t] #буква шифртекста
                        decode_text = decode_text + decode_letter #шифртекст
                    else:    
                        decode_letter = alphavite_eng[number_t] #буква открытого текста
                        decode_text = decode_text + decode_letter #открытый текст
                elif i not in alphavite_eng:   
                    decode_text = decode_text + i
            print(decode_text)
            input()
        
        elif decode_mod == '2' or decode_mod == "bf":
            decode_text = ""
            text = input("Введите текст для расшифровки: ")
            key = range(1, (len(alphavite_eng)))
            for j in key:
                for i in text.lower(): 
                    if i in alphavite_eng:
                        number_t = alphavite_eng.index(i) + j #индекс буквы шифртекста
                        i.lower()
                        if number_t >= len(alphavite_eng) - 1:
                            number_t = len(alphavite_eng) - number_t  #индекс буквы шифртекста
                            decode_letter = alphavite_eng[-number_t] #буква шифртекста
                            decode_text = decode_text + decode_letter #шифртекст
                        else:    
                            decode_letter = alphavite_eng[number_t] #буква открытого текста
                            decode_text = decode_text + decode_letter #открытый текст
                    elif i not in alphavite_eng:   
                        decode_text = decode_text + i
                print("ROT" + str(j) +  ": " + decode_text[-len(text):] + "\n")
                input()
