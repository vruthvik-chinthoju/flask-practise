from sqlalchemy import insert,select,update,delete
from connection import manager,employee,engine


# def create_engine(manager_name,manager_email):
#     sql_statement = insert(manager).values(manager_name=manager_name,manager_email=manager_email)
#     with engine.connect() as conn:
#         conn.execute(sql_statement)
#         conn.commit()



# create_engine('Luffy','luffy@gmail.com')
# create_engine('Zoro','zoro@gmail.com')
# create_engine('Sanji','sanji@gmail.com')
# create_engine('Ussop','ussop@gmail.com')
# create_engine('Robin','robin@gmail.com')


def read_one_data(id):
    sql_statement = select(manager).where(manager.c.id==id)
    with engine.connect() as conn:
        print(sql_statement)
        conn.execute(sql_statement)
        conn.commit()


read_one_data(1)

