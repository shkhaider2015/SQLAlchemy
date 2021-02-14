# from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
# from sqlalchemy.ext.declarative import declarative_base


# base = declarative_base()

# class Person(base):
#     __tablename__ = "person"
#     id = Column('id', Integer, primary_key=True)
#     username = Column('username', String, unique=True)


# engine = create_engine('sqlite:///:users.db', echo=True)
# base.metadata.create_all(bind=engine)

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String),
)
meta.create_all(engine)