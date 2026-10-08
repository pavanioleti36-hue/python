from abc import ABC, abstractmethod
class database(ABC):
    @abstractmethod
    def connect(self):
        pass
class sqldb(database):
    def connect(self):
        print("sql database is connected")
class mongodb(database):
    def connect(self):
        print("mongodb databse is connected")
dbs= [sqldb(), mongodb()]
for db in dbs:
    db.connect()