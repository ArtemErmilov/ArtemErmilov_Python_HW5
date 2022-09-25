# Задача 1.
# - Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"


from os import system
system ('cls')
import Base

def deleting_text(tex_del:str,text_in:str) :

    list_in= text_in.split()

    list_out = []

    for text in list_in:
        if text.count(tex_del)==0:
            list_out.append(text)
    return ' '.join(list_out) 



my_text = 'абвгдейка - это передача'

new_text = deleting_text('абв',my_text)




print (f'{my_text}  = > {new_text}')
    