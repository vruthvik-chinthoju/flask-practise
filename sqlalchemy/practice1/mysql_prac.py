from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/m100',echo=True)

meta = MetaData()



employee = Table('employee',meta,
                 Column('id',Integer,primary_key=True,unique=True,autoincrement=True),
                 Column('name',String(150),nullable=False),
                 Column('email',String(150),nullable=False,unique=True),
                 Column('department',String(150),nullable=True)
                 )

meta.create_all(bind=engine) 









