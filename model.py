import time
import os
import json
import settings

# class Record():
#
#     def __init__(self
#                  , id = 0
#                  , title = ''
#                  , note = ''
#                  , datetime = time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))
#                  ):
#         self._id = id
#         self._title = title
#         self._note = note
#         self._datetime = datetime
#
#     def get_id(self) -> int:
#         return self._id
#     def set_id(self,id):
#         self._id = id
#
#     def get_title(self) -> str:
#         return self._title
#     def set_title(self, title):
#         self._title = title
#
#     def get_note(self) -> str:
#         return self._note
#     def set_note(self, note):
#         self._note = note
#
#     def get_datetime(self) -> time.time:
#         return self._datetime
#     def set_datetime(self, datetime):
#         self._datetime = datetime
#
#     def get_dict(self):
#         return { "id": self.get_id(),
#                  "title": self.get_title(),
#                  "note": self.get_note(),
#                  "datetime": self.get_datetime()
#                }

class Data():
    def __init__(self):
        self._data = []

    def get_length(self):
        return len(self._data)

    def add(self,title, note):
        #record = Record(len(self._data),title = title, note = note)
        #self._data.append(record)
        self._data.append({"id": self.get_length(),
                           "title": title,
                           "note": note,
                           "datetime": time.strftime("%Y.%m.%d %H:%M:%S",time.gmtime(time.time()))
                           })

        # self._data.append(Record(len(self._data),title = title, note = note))
    def get(self, n):
        return self._data[n]

    def save_db(self):
        if self.get_length() > 0:
            with open(settings.db_file, 'w', encoding='UTF-8') as f:
#                json.dump([i.get_dict() for i in self._data],f)
                json.dump(self._data,f)

    def load_db(self):
        if os.path.isfile(settings.db_file):
            with open(settings.db_file, 'r', encoding='UTF-8') as f:
                self._data.clear()
                self._data = json.load(f)

