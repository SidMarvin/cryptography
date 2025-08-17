alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphavite_eng = "abcdefghijklmnopqrstuvwxyz"

mod = input("Выбран шифр A1Z26. Выберите действие:\n[1] Зашифровать\n[2] Расшифровать\n: ")

if mod == "1" or mod == "e":
    text_lang = input("Выберите язык для зашифрования\n[1] Русский\n[2] Английский\n: ")
    if text_lang == "1":
        encode_text = ""
        text = input("Введите текст для зашифрования: ")
        for i in text.lower():
            if i in alphavite_rus:
                number = str(alphavite_rus.index(i) + 1) + "-"
                encode_text = encode_text + number
                    
            elif i not in alphavite_rus:
                if i == " ":
                    encode_text = encode_text + i
                elif i == ",":
                    encode_text = encode_text + i
                elif i == "?":
                    encode_text = encode_text + i
                elif i == "!":
                    encode_text = encode_text + i
                elif i == ":":
                    encode_text = encode_text + i
                elif i == ".":
                    encode_text = encode_text + i 

        #прописать алгоритм просмотра текста и удаления последнего символа в слове
        words = encode_text.split()
        # Удаляем последнюю букву в каждом слове и создаем новый список слов
        modified_words = [word[:-1] if len(word) > 0 else word for word in words]
        # Соединяем слова обратно в текст
        modified_text = ' '.join(modified_words)
        print(modified_text)
        


    elif text_lang == "2":
        encode_text = ""
        text = input("Введите текст для зашифрования: ")
        for i in text.lower():
            if i in alphavite_eng:
                number = str(alphavite_eng.index(i) + 1) + "-"
                encode_text = encode_text + number
               
            elif i not in alphavite_eng:
                if i == " ":
                    encode_text = encode_text + i
                elif i == ",":
                    encode_text = encode_text + i
                elif i == "?":
                    encode_text = encode_text + i
                elif i == "!":
                    encode_text = encode_text + i
                elif i == ":":
                    encode_text = encode_text + i
                elif i == ".":
                    encode_text = encode_text + i                    

        #прописать алгоритм просмотра текста и удаления последнего символа в слове
        words = encode_text.split()
        # Удаляем последнюю букву в каждом слове и создаем новый список слов
        modified_words = [word[:-1] if len(word) > 0 else word for word in words]
        # Соединяем слова обратно в текст
        modified_text = ' '.join(modified_words)
        print(modified_text)
    
    
elif mod == "2" or mod == "d":
    decode_text = ""
    decode_letter = ""
    decode_word = ""
    text_lang = input("Выберите язык для зашифрования\n[1] Русский\n[2] Английский\n: ")
    if text_lang == "1":
        text = input("Введите текст для расшифрования: ")
        text = text.split() #делим строку по пробелам на список с цифрами
        for words in text:
            words = words.split("-") #делим элементы списка на списки по дефису
            count = len(words)
            for symbols in words:
                count -= 1
                if count > 0:
                    decode_text = decode_text + alphavite_rus[int(symbols)-1]
                elif count == 0:
                    decode_text = decode_text + alphavite_rus[int(symbols)-1] + " " 
        print(decode_text)
        
    elif text_lang == "2":
        text = input("Введите текст для расшифрования: ")
        text = text.split() #делим строку по пробелам на список с цифрами
        for words in text:
            words = words.split("-") #делим элементы списка на списки по дефису
            count = len(words)
            for symbols in words:
                count -= 1
                if count > 0:
                    decode_text = decode_text + alphavite_eng[int(symbols)-1]
                elif count == 0:
                    decode_text = decode_text + alphavite_eng[int(symbols)-1] + " " 
        print(decode_text)
   