alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphavite_eng = "abcdefghijklmnopqrstuvwxyz"

mod = input("Выбран шифр Атбааш. Выберите действие:\n[1] Зашифровать\n[2] Расшифровать\n:  ")

if mod == "1" or mod == "e":
    encode_text = ""
    text_lang = input("Выберите язык для зашифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        text = input("Введите текст для зашифрования: ")
        length_alphabet = len(alphavite_rus)
        for i in text.lower():
            if i in alphavite_rus:
                number_t = alphavite_rus.index(i) #индекс буквы открытого текста
                crypt_symbol_index = (length_alphabet - number_t) - 1 #индекс буквы закрытого текста
                encode_text = encode_text + alphavite_rus[crypt_symbol_index]
            elif i not in alphavite_rus: 
                encode_text = encode_text + i          
        print(encode_text)
    
    elif text_lang == "2":
        text = input("Введите текст для расшифрования: ")
        length_alphabet = len(alphavite_eng)
        for i in text.lower():
            if i in alphavite_eng:
                number_t = alphavite_eng.index(i) #индекс буквы открытого текста
                crypt_symbol_index = (length_alphabet - number_t) - 1 #индекс буквы закрытого текста
                encode_text = encode_text + alphavite_eng[crypt_symbol_index]
            elif i not in alphavite_eng: 
                encode_text = encode_text + i          
        print(encode_text)
    
elif mod == "2" or mod == "d":
    decode_text = ""
    text_lang = input("Выберите язык для зашифрования: \n[1] Русский \n[2] Английский\n: ")
    if text_lang == "1":
        text = input("Введите текст для зашифрования: ")
        length_alphabet = len(alphavite_rus)
        for i in text.lower():
            if i in alphavite_rus:
                number_t = alphavite_rus.index(i) #индекс буквы открытого текста
                crypt_symbol_index = (length_alphabet - number_t) - 1 #индекс буквы закрытого текста
                decode_text = decode_text + alphavite_rus[crypt_symbol_index]
            elif i not in alphavite_rus: 
                decode_text = decode_text + i          
        print(decode_text)
    
    elif text_lang == "2":
        text = input("Введите текст для зашифрования: ")
        length_alphabet = len(alphavite_eng)
        for i in text.lower():
            if i in alphavite_eng:
                number_t = alphavite_eng.index(i) #индекс буквы открытого текста
                crypt_symbol_index = (length_alphabet - number_t) - 1 #индекс буквы закрытого текста
                decode_text = decode_text + alphavite_eng[crypt_symbol_index]
            elif i not in alphavite_eng: 
                decode_text = decode_text + i          
        print(decode_text)