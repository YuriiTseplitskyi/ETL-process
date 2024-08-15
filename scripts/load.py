import os
import psycopg2
import pandas as pd
from config.db_config import DB_PARAMS


TRANSFORMED_CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_data.csv')


def connect_to_db(db_params):
    conn = psycopg2.connect(
        dbname=db_params['dbname'],
        user=db_params['user'],
        password=db_params['password'],
        host=db_params['host'],
        port=db_params['port']
    )
    return conn


def insert_data_into_db(conn, df):

    with conn.cursor() as cur:
        for _, row in df.iterrows():
            cur.execute('''
                INSERT INTO "Users" (name, email, signup_date, domain)
                VALUES (%s, %s, %s, %s)
                ON CONFLICT (email) DO NOTHING;
            ''', (row['name'], row['email'], row['signup_date'], row['domain']))
        conn.commit()


def main():

    df = pd.read_csv(TRANSFORMED_CSV_FILE)
    conn = connect_to_db(DB_PARAMS)
    try:
        insert_data_into_db(conn, df)
        print("Transformed data inserted into the PostgreSQL table.")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
