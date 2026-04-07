from sqlalchemy import create_engine, text

database=create_engine('postgresql://postgres:prajwal@localhost:5432/Subscription management system')

with database.connect() as connection:
    result = connection.execute(text("SELECT * FROM users;"))
    for row in result:
        print(row)

connection.close()