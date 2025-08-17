#находим индекс совпадений
"""https://habr.com/ru/articles/876764/
https://planetcalc.ru/2468/
https://planetcalc.com/8550/"""

import re

alphavite_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

text = input("Введите текст для анализа: ")
action = input("Выберите дейсвтие: \n[1] Индекс совпадений \n[2] Частотный анализ\n[3] Энтропия текста\n:")
num = 0

text = text.lower()
text = re.sub(r'[.,!?:\s-]', '', text) #удаляем посторонние знаки

#индекс совпадений
def index_of_coincidence(text):
    IOC = 0
    l_i_squared = 0
    for i in range(0, len(alphavite_rus)):
        l_i = text.count(alphavite_rus[i]) #кол-во букв с одинаковым индексом
        l = len(text) #кол-во букв в шифртексте
        l_i_squared += l_i**2 
        IOC = (1/l**2) * l_i_squared
    print("Индекс совпадений равен: " + str(IOC))
    input()

#частотный анализ
def frequency_analysis(text):
    for i in range(0, len(alphavite_rus)):
        symbol = text.count(alphavite_rus[i])
        len_text = len(text)
        frequency_analysis = round((100*symbol)/len_text, 2)
        print(f"Символ {alphavite_rus[i]} - {frequency_analysis}%")
    
    
if action == "1":
    index_of_coincidence(text)
elif action == "2":
    frequency_analysis(text)
