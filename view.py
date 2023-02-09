import time
from log import add2log

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
        print('\t /list - вывод списка дел')
        print('\t /add  - добавить новую заметку')
        print('\t /edit - редактировать заметку')
        print('\t /del  - удалить заметку')
        print('\t /save - принудительно сохранить базу в файл')

    def add_edit(self, save_title = '', save_note = ''):
        print('Добавление записи')
        title: str = input('Введите заголовок заметки: ')
        note: str = input('Описание заметки: ')

        title = save_title if len(title) == 0 else title
        note = save_note if len(note) == 0 else note

        print('Данные добавлены')
        add2log('Добавление данных:', '<')
        add2log(f'Title = {title}; Note = {note} ', '<')
        return (title, note)
