from sqlalchemy import insert,select,update,delete
from connection import manager,employee,engine
# from connection import Employee

def create_engine(emp_name,related_mgr):
    sql_statement = insert(employee).values(emp_name=emp_name,related_mgr=related_mgr)
    with engine.connect() as conn:
        conn.execute(sql_statement)
        conn.commit()


# create_engine('Jhonny',2)
# create_engine('Osaku',2)
# create_engine('Bartoloemo',1)
# create_engine('Leo',1)

create_engine('Cabbage',1)