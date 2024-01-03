from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Parent(Base):
    __tablename__ = 'parents'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    children = relationship('Child', foreign_keys='Child.parent_id')

class Child(Base):
    __tablename__ = 'children'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    parent_id = Column(Integer, ForeignKey('parents.id'))

# Creating the database engine
engine = create_engine('sqlite:///:memory:')

# Creating the tables
Base.metadata.create_all(engine)
# Creating instances
parent = Parent(name='Parent 1')
child = Child(name='Child 1')

# Adding child to parent
parent.children.append(child)

# Setting parent for the child explicitly
child.parent = parent
