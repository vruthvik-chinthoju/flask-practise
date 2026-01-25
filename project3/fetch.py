import mysql.connector

class Data:

    conn=mysql.connector.connect(
        user='root',
        password='root',
        host='localhost',
        database='office'
    )
    cursor=conn.cursor()
    

    # def fetch(self):
    #     query='select * from manager'
    #     self.cursor.execute(query)
    #     data=self.cursor.fetchall()


    def all_employees(self,emp_data=0):
        query='select * from employee'
        self.cursor.execute(query)
        all= self.cursor.fetchall()
        for row in all:
            print(row)
        print("---DATA OF ALL EMPLOYEES-----------------")    
        emp_data=all
        return emp_data



obj1=Data()
# obj1.fetch()
print(obj1.all_employees())

