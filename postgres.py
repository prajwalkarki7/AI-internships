from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine, Column, Integer, String

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String) 
    age=Column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, name='{self.name}', age={self.age})"

engine = create_engine('sqlite:///users.db', echo=True) #database connection
Base.metadata.create_all(engine) #database migration

with Session(engine) as session:
    new_user = User(name='Alice', age=30)
    session.add(new_user)
    session.commit()

    users = session.query(User).all()
    for user in users:
        print(user)
