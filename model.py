import time

class Record():

    def __init__(self, id = 0, title = '', note = '', datetime = time.time()):
        self._id = id
        self._title = title
        self._note = note
        self._datetime = datetime

    def get_id(self) -> int:
        return self._id
    def set_id(self,id):
        self._id = id

    def get_title(self) -> str:
        return self._title
    def set_title(self, title):
        self._title = title

    def get_note(self) -> str:
        return self._note
    def set_note(self, note):
        self._note = note

    def get_datetime(self) -> time.time:
        return self._datetime
    def set_datetime(self, datetime):
        self._datetime = datetime

class Data():
    def __init__(self):
        pass
