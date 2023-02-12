import time
import os
import json

import settings


class Data:
    _data: []

    def __init__(self):
        self._data = []

    def get_length(self):
        return len(self._data)

    def add(self, title, note):
        self._data.append({"id": self.get_max_id() + 1,
                           "title": title,
                           "note": note,
                           "datetime": time.strftime("%Y.%m.%d %H:%M:%S", time.gmtime(time.time()))
                           })

    def get(self, n):
        return self._data[n]

    def save_db(self):
        if self.get_length() > 0:
            with open(settings.db_file, 'w', encoding='UTF-8') as f:
                json.dump(self._data,f)

    def load_db(self):
        if os.path.isfile(settings.db_file):
            with open(settings.db_file, 'r', encoding='UTF-8') as f:
                self._data.clear()
                self._data = json.load(f)

    def delete(self, idx):
        pointer = -1
        for i in range(self.get_length()):
            if idx == int(self._data[i]["id"]):
                pointer = i
                break
        if pointer == -1:
            return -1
        else:
            del self._data[idx]
            return 0

    def get_max_id(self):
        return max([i["id"] for i in self._data])

    def edit(self, idx, title, note):
        pointer = -1
        for i in range(self.get_length()):
            if idx == int(self._data[i]["id"]):
                pointer = i
                break
        if pointer == -1:
            return -1
        else:
            if len(title) > 0: self._data[idx]['title'] = title
            if len(note) > 0: self._data[idx]['note'] = note
            self._data[idx]['datetime'] = time.strftime("%Y.%m.%d %H:%M:%S", time.gmtime(time.time()))
            return 0
