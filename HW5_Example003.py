# Задача 3
# Создайте два списка — один с названиями языков программирования, 
# другой — с числами от 1 до длины первого.

# ['python', 'c#']
# [1,2]

# Вам нужно сделать две функции: первая из которых создаст список кортежей, 
# состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]

# Вторая — которая отфильтрует этот список следующим образом:
# если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, 
# то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]

# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове.
# Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с
#  преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&

import unicodedata
from codecs import utf_16_be_decode
import numbers
from os import system
system ('cls')
import Base


language_program_txt = 'Java C# C Python C++ Go JavaScript PHP Scratch Fortran'

language_program_list = language_program_txt.split()
number_program_list = [1,2,3,4,5,6,7,8,9,10]



data_program = list(zip(number_program_list, [text.upper() for text in language_program_list]))


list_index =[]
list_text = []

for kor in data_program:
    for data in reversed(kor):
        if kor.index(data)==0:
            sum_letter = str(sum(list(map(lambda x: ord(x),(letter for letter in text_)))))
            if sum_letter.count(str(data)) >0:
                list_index.append(int(sum_letter))
            else:
                list_index.append(data)
        else:
            text_ = data
            list_text.append(data)

new_data_program=list(zip(list_index,list_text))

print(data_program)
print('--'*50)
print (new_data_program)