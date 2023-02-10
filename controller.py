from view import View
from model import Data
from log import add2log

class Controller(object):
    def __init__(self):
        self._view = View()
        self._data = []

    def add(self):
        pass

    def run(self):
        self._view.info()
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
                case _ :
                    print('Неверная команда. Для помощи наберите /help')
        self._view.buy()
        add2log('Завершение работы.','>')
