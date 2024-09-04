import os

NUM_RECORDS = 1000
CSV_HEADERS = ['user_id', 'name', 'email', 'signup_date']

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CSV_FILE_PATH = os.path.join(OUTPUT_DIR, 'data.csv')
TRANSFORMED_CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_data.csv')
INPUT_CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
