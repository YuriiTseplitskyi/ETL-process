import pandas as pd
import psycopg2
from config.db_config import DB_PARAMS
import os


#transformed_csv_file = 'C:\\MAIN\\it\\projects\\py\\InforceTestTask\\data\\transformed_data.csv'
transformed_csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_data.csv')
df = pd.read_csv(transformed_csv_file)

conn = psycopg2.connect(
    dbname=DB_PARAMS['dbname'],
    user=DB_PARAMS['user'],
    password=DB_PARAMS['password'],
    host=DB_PARAMS['host'],
    port=DB_PARAMS['port']
)
cur = conn.cursor()

for index, row in df.iterrows():
    cur.execute('''
        INSERT INTO "Users" (name, email, signup_date, domain)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (user_id) DO NOTHING;
    ''', (row['name'], row['email'], row['signup_date'], row['domain']))

conn.commit()
cur.close()
conn.close()

print("Transformed data inserted into the PostgreSQL table.")
