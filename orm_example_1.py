# -*- encoding: utf-8 -*-
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()

class Foo(Base):
	__tablename__ = 'Foo'

	id = Column('id', Integer, primary_key=True)
	fooname = Column('fooname', String(50))



if __name__ == "__main__":
	engine = create_engine('mysql://<user>:<password>@127.0.0.1/<database>')
	Base.metadata.create_all(bind=engine)
	Session = sessionmaker(bind=engine)


