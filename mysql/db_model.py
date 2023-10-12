from __future__ import unicode_literals, absolute_import
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, BigInteger, Integer, String, DateTime
# from sqlalchemy.orm import relationship

ModelBase = declarative_base()


class User(ModelBase):
    __tablename__ = "users"
    id = Column(BigInteger, primary_key=True)
    name = Column(String(length=20))
    password = Column(String(length=20))
    status = Column(Integer)
    create_date = Column(DateTime)

