from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker

# engine = create_engine('postgresql+psycopg2://postgres:root@localhost:5432/m100')
engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/m100',echo=True)
Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    cust_id = Column(Integer,primary_key=True,nullable=False,unique=True,autoincrement=True)
    cust_name = Column(String(150),nullable=False)
    cust_email = Column(String(150),unique=True,nullable=False)



    def __str__(self):
        return f"""{"-"*40}
name  :{self.cust_name}
email :{self.cust_email}
{"-"*40}"""


Base.metadata.create_all(engine)
Session =sessionmaker(bind=engine)
session = Session()


