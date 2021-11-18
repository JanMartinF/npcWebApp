import psycopg2
from config import config
def testfunction():
    connection = None
    commands = (
        """
        CREATE TABLE cities (
            id serial,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            PRIMARY KEY (id)
        )
        """,
        """
        CREATE TABLE npcs (
            id serial,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            city_id INT,
            PRIMARY KEY (id),
            FOREIGN KEY (city_id) REFERENCES cities(id)
        )
        """
    )
    try:
        print('connecting to DB')
        dbLogInDetail = config()
        connection = psycopg2.connect(**dbLogInDetail)

        cursor = connection.cursor()
        for command in commands:
            cursor.execute(command)
            print("command executed")
        cursor.close()
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print('exception!')
        print(error)
        pass
    if connection is not None:
        connection.close()
        print('DB connection closed')
    return 
testfunction()




