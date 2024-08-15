import csv
import os
from faker import Faker

NUM_RECORDS = 1000
CSV_HEADERS = ['user_id', 'name', 'email', 'signup_date']
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
CSV_FILE_PATH = os.path.join(OUTPUT_DIR, 'data.csv')

fake = Faker()


def generate_fake_record(record_id):

    return {
        'user_id': record_id,
        'name': fake.name(),
        'email': fake.email(),
        'signup_date': fake.date_time_between(start_date='-5y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
    }


def write_csv(file_path, headers, records):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(records)


def main():

    records = [generate_fake_record(i) for i in range(1, NUM_RECORDS + 1)]
    write_csv(CSV_FILE_PATH, CSV_HEADERS, records)
    print(f'CSV file "{CSV_FILE_PATH}" with {NUM_RECORDS} records created successfully.')


if __name__ == "__main__":
    main()
