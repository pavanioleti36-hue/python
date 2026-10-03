from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    @abstractmethod
    def insert(self, data):
        pass
    @abstractmethod
    def close(self):
        pass
class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")
    def insert(self, data):
        print("Inserted", data, "into MySQL")
    def close(self):
        print("MySQL connection closed")
class MongoDB(Database):
    def connect(self):
        print("Connected to MongoDB")
    def insert(self, data):
        print("Inserted", data, "into MongoDB")
    def close(self):
        print("MongoDB connection closed")
mysql = MySQL()
mysql.connect()
mysql.insert("Employee")
mysql.close()
print()
mongo = MongoDB()
mongo.connect()
mongo.insert("Student")
mongo.close()