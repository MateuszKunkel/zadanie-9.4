import json


class Records:
    def __init__(self):
        try:
            with open("books.json", "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []

    def all(self):
        return self.records

    def get(self, id):
        record = [record for record in self.all() if record["id"] == id]
        if record:
            return record[0]
        return []

    def create(self, data):
        data.pop('csrf_token')
        self.records.append(data)
        self.save_all()

    def update(self, id, data):
        data.pop('csrf_token')
        record = self.get(id)
        if record:
            index = self.records.index(record)
            self.records[index] = data
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("books.json", "w") as f:
            json.dump(self.records, f)


records = Records()
