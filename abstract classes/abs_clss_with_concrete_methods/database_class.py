from abc import ABC, abstractmethod
class Database(ABC):
    @abstractmethod
    def connect(self):
        pass
    def display_database_name(self):
        print("Database: MySQL")
class MySQL(Database):
    def connect(self):
        print("Connected to MySQL")
class PostgreSQL(Database):
    def connect(self):
        print("Connected to PostgreSQL")
m = MySQL()
p = PostgreSQL()
m.connect()
m.display_database_name()
p.connect()
p.display_database_name()