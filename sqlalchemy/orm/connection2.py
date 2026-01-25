# from sqlalchemy import create_engine,Column,Intger,String
# from sqlalchemy.orm import declarative_base,sessionmaker


# engine = create_engine('mysql+mysqlconnector://root:root@localhost:3306/m100',echo=True)
# Base = declarative_base()

# class Onepiece(Base):
#     __tablename__='onepiece'
#     id = Column(Intger,primary_key=True,unique=True,autoincrement=True,nullable=False)
#     name = Column(String(150),nullable=False,unique=True)
#     role = Column(String(150),nullable=False)
#     age = Column(Intger,nullable=False)


# Base.metadata.create_all(engine)
# Session = sessionmaker(bind=engine)
# session = Session()

    