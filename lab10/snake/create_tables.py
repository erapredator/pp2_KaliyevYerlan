#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE users (
            login TEXT PRIMARY KEY,
            level INTEGER,
            max_score INTEGER
        )
        """,
        """
        CREATE TABLE saved_state (
            id_login TEXT REFERENCES users(login),
            snake_pos POINT[],
            current_score INTEGER,
            dx INTEGER = 0,
            dy INTEGER = 0
        )
        """)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        for command in commands:
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