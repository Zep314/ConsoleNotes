import time
from log import add2log
from model import Data
#from model import Record

class View():
    def __init__(self):
        pass

    def info(self):
       print('Программа для ведения заметок')
       print('Выполнена в качестве проекта промежуточной аттестации')
       print('на побразовательном портале GeekBrains')
       print('Морданов Д.А. 2023г.')

    def buy(self):
        print('Работа программы завершена.')

    def help(self):
        print('Обрабатываются следующие команды:')
        print('\t /help - вывод помощи')
        print('\t /info - вывод информации о программе')
        print('\t /exit или /quit - выход из программы')
        print('\t /list - вывод списка заметок')
        print('\t /add  - добавить новую заметку')
        print('\t /edit - редактировать заметку')
        print('\t /del  - удалить заметку')
        print('\t /save - принудительно сохранить базу в файл')

    def add(self):
        print('Добавление записи')
        title: str = input('Введите заголовок заметки: ')
        note: str = input('Описание заметки: ')
        return (title, note)

    def print(self,text):
        print(text)

    def show_records(self,data): # Отображение всей базы на экране красиво
        list = data._data
        print(f'{"-"*1}Номер{"-"*1}+{"-"*11}Заголовок{"-"*10}+{"-"*26}Заметка{"-"*26}+{"-"*7}Время{"-"*7}')

        for i in range(data.get_length()):
            print(f'{list[i]["id"]:7}|{list[i]["title"]:30}|{list[i]["note"]:59}|{list[i]["datetime"]:11}')

        print(f'{"-"*7}+{"-"*30}+{"-"*59}+{"-"*19}')

    def select_record(self):
        return input('Введите номер записи для удаления, или -1 - для отмены действия: ')