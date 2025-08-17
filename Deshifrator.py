open_text = input("Введите текст для шифрования/дешифрования: ")
open_symbol = input("Введите символы, которые нужно заменить: ")
close_symbol = input("Введите символы, НА которые нужно заменить: ")


if len(open_symbol) != len(close_symbol):
    print("Ошибка: количество символов для замены должно совпадать с количеством символов-заменителей.")
else:
    shifr_table = str.maketrans(open_symbol, close_symbol)
    close_text = open_text.translate(shifr_table)
    print(close_text)
