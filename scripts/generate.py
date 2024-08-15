import csv
import faker
import os

fake = faker.Faker()

num_records = 1000

#'C:\\MAIN\\it\\projects\\py\\InforceTestTask\\data\\data.csv'
csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    writer.writerow(['user_id', 'name', 'email', 'signup_date'])

    for i in range(1, num_records + 1):
        user_id = i
        name = fake.name()
        email = fake.email()
        signup_date = fake.date_time_between(start_date='-5y', end_date='now').strftime('%Y-%m-%d %H:%M:%S')
        writer.writerow([user_id, name, email, signup_date])

print(f'CSV file "{csv_file}" with {num_records} records created successfully.')