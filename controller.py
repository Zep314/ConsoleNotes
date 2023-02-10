from view import View
from model import Data
from log import add2log


class Controller(object):
    def __init__(self):
        self._view = View()
        self._data = Data()

    def add(self):
        self._view.print('Добавление записи')
        title, note = self._view.add_edit()
        self._data.add(title, note)
        self._view.print('Данные добавлены')
        add2log('Добавление данных:', '<')
        add2log(f'Title = {title}; Note = {note} ', '<')

    def list(self):
        self._view.show_records(self._data)
        add2log(f'Выведено {self._data.get_length()} строк базы данных', '<')

    def load(self):
        self._data.load_db()
        self._view.print("Данные загружены из файла!")
        add2log("Данные загружены из файла.", '>')

    def save(self):
        self._data.save_db()
        self._view.print("Данные записаны в файл!")
        add2log("Данные записаны в файл.", '>')

    def delete(self):
        idx = int(self._view.select_record())
        if idx > -1:
            if self._data.delete(idx) != -1:
                self._view.print(f"Запись {idx} удалена!")
                add2log(f"Запись {idx} удалена!",">")
            else:
                self._view.print("Ошибка! Записи с таким индексом для удаления не найдено!")
                add2log(f"Ошибка удаления записи {str(idx)}. Записи не существует!",">")
    def edit(self):
        idx = int(self._view.select_record())
        if idx > -1:
            self._view.print('Редактирование записи')
            self._view.print('Если данные менять не нужно - оставьте их пустыми')
            title, note = self._view.add_edit()
            if self._data.edit(idx, title, note) != -1:
                self._view.print(f"Запись {idx} успешно изменена! title => {title}, note => {note}")
                add2log(f"Запись {idx} изменена! title => {title}, note => {note}", ">")
            else:
                self._view.print("Ошибка! Записи с таким индексом для редактирования не найдено!")
                add2log(f"Ошибка редактирования записи {str(idx)}. Записи не существует!",">")

    def run(self):
        self._view.info()
        self.load()
        while True:
            inp = input('>>> ')
            add2log(inp, '>')  # Записываем в журнал все, что вводят
            match inp.lower():
                case '/exit':
                    break
                case '/quit':
                    break
                case '/help':
                    self._view.help()
                case '/add':
                    self.add()
                case '/edit':
                    self.edit()
                case '/del':
                    self.delete()
                case '/list':
                    self.list()
                case '/save':
                    self.save()
                case '/load':
                    self.load()
                case _:
                    self._view.print('Неверная команда. Для помощи наберите /help')
        self._view.buy()
#        self.save()
        add2log('Завершение работы.', '>')
