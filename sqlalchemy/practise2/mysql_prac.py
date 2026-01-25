from sqlalchemy import create_engine,MetaData,Table,Column,Integer

engine = create_engine('')

meta =MetaData()

student = Table('Student',meta,
                Column('rollno',Integer,primary_key=True,nullable=True,autoincrement=True),
                Column(''))

