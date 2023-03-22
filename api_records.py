import json

class Api_Records:
    def __init__(self):
        try:
            with open("records.json", "r") as f:
                self.records = json.load(f)
        except FileNotFoundError:
            self.records = []

    def all(self):
        return self.records

    def get(self, id):
        record = [record for record in self.all() if record['id'] == id]
        if record:
            return record[0]
        return []

    def create(self, data):
        self.records.append(data)
        self.save_all()

    def update(self, id, data):
        record = self.get(id)
        if record:
            index = self.records.index(record)
            self.records[index] = data
            self.save_all()
            return True
        return False

    def delete(self, id):
        record = self.get(id)
        if record:
            self.records.remove(record)
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("records.json", "w") as f:
            json.dump(self.records, f)

api_records = Api_Records()