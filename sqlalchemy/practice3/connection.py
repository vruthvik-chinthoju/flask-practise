from sqlalchemy import create_engine,MetaData,Table,Column,Integer,String,ForeignKey

engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/m100',echo=True)

meta = MetaData()

manager = Table('manager',meta,
             Column('id',Integer,primary_key=True,unique=True,nullable=False,autoincrement=True),
             Column('manager_name',String(150),nullable=False),
             Column('manager_email',String(150),nullable=False,unique=True))

employee = Table('employee',meta,
                 Column('emp_id',Integer,primary_key=True,unique=True,nullable=False,autoincrement=True),
                 Column('emp_name',String(150),nullable=False),
                 Column('related_mgr',Integer,ForeignKey('manager.id',ondelete='CASCADE',onupdate='CASCADE'),nullable=False))

meta.create_all(bind=engine)



