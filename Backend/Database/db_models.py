from sqlalchemy import Table, create_engine, ForeignKey, Column, Integer, Float, BLOB,Boolean, DATETIME, String, LargeBinary, DateTime, Text, func
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship

# Create a base class for declarative models
Base = declarative_base()

class Khu(Base):
    __tablename__ = 'khu'
    id = Column(Integer, primary_key=True)
    ten = Column(String)
    phongs = relationship("Phong", back_populates="khu")

class Phong(Base):
    __tablename__ = 'phong'
    id = Column(Integer, primary_key=True)
    ten = Column(String)
    khu_id = Column(Integer, ForeignKey('khu.id'))
    don_vi_id = Column(Integer, ForeignKey('don_vi.id'))
    # Relationships
    khu = relationship("Khu", back_populates="phongs")
    don_vi = relationship("DonVi")

class DonVi(Base):
    __tablename__ = "don_vi"
    id = Column(Integer, primary_key=True)
    ten = Column(String)
    phongs = relationship("Phong")



"""
# One-to-one
class Citizen(Base):

    __tablename__ = "citizen"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)

    # Relationships
    passport = relationship("Passport")

class Passport(Base):

    __tablename__ = "passport"

    id = Column(Integer, primary_key=True)
    citizen_id = Column(Integer, ForeignKey("citizen.id"))
    passport_id = Column(String(25), unique=True, nullable=False)

    # Relationships
    citizen = relationship("Citizen")

# One-to-many
class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    orders = relationship("Order", back_populates="customer")

class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey('customer.id'))

    # Relationship
    customer = relationship("Customer", back_populates="orders")

# For example, to get the orders for a customer, we can write:
customer = session.query(Customer).get(1)
orders = customer.orders

# For example, to get the customer for an order, we can write:
order = session.query(Order).get(1)
customer = order.customer

Many-to-many
class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship
    courses = relationship("Course", secondary="student_course", back_populates="students")

class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String)

    # Relationship
    students = relationship("Student", secondary="student_course", back_populates="courses")

class StudentCourse(Base):
    __tablename__ = 'student_course'
    student_id = Column(Integer, ForeignKey('student.id'), primary_key=True)
    course_id = Column(Integer, ForeignKey('course.id'), primary_key=True)

# For example, to get the courses for a student, we can write:
student = session.query(Student).get(1)
courses = student.courses
"""

"""
Sure! Here are some examples of how you can perform CRUD operations on the Users and Clients models with the many-to-many relationship:

Create a new user and associate it with one or more clients:
python
Copy code
# Create a new user
new_user = Users(username='john', password='password123', role='admin')

# Add clients to the user's clients list
client1 = Clients(id=b'client1')
client2 = Clients(id=b'client2')
new_user.clients.extend([client1, client2])

# Add the user to the session and commit the changes
session.add(new_user)
session.commit()
Get all clients associated with a specific user:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Access the associated clients using the clients attribute
clients = user.clients
for client in clients:
    print(client.id)
Add a new client and associate it with one or more existing users:
python
Copy code
# Create a new client
new_client = Clients(id=b'client3')

# Get existing users
users = session.query(Users).filter(Users.username.in_(['john', 'alice'])).all()

# Add the new client to each user's clients list
for user in users:
    user.clients.append(new_client)

# Commit the changes
session.commit()
Remove a client from a user's clients list:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Remove a client from the user's clients list
client_to_remove = session.query(Clients).filter_by(id=b'client1').first()
user.clients.remove(client_to_remove)

# Commit the changes
session.commit()
Delete a user and automatically remove the association with clients:
python
Copy code
# Get a specific user by username
user = session.query(Users).filter_by(username='john').first()

# Delete the user
session.delete(user)

# Commit the changes
session.commit()
These examples demonstrate how to create, read, update, and delete data in the Users and Clients models while maintaining the many-to-many relationship.
"""