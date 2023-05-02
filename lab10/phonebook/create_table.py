import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    command = (
        """
        CREATE TABLE phonebook (
            name VARCHAR(255) NOT NULL,
            number VARCHAR(255) NOT NULL
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()