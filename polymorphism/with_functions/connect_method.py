class sqldb:
    def connect(self):
        print("SQL Database connects to the application")
class phpdb:
    def connect(self):
        print("PHP Database connects to the application")
class mysqldb:
    def connect(self):
        print("MySQL Database connects to the application")
def assign_connect(employee):
    employee.connect()
sql_db = sqldb()
php_db = phpdb()
mysql_db = mysqldb()
assign_connect(sql_db)
assign_connect(php_db)
assign_connect(mysql_db)