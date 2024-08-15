import pandas as pd
import re
import os

#csv_file = 'C:\\MAIN\\it\\projects\\py\\InforceTestTask\\data\\data.csv'
csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')

df = pd.read_csv(csv_file)

df['signup_date'] = pd.to_datetime(df['signup_date']).dt.strftime('%Y-%m-%d')

def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

df = df[df['email'].apply(is_valid_email)]

df['domain'] = df['email'].apply(lambda x: x.split('@')[-1])

print("\nTransformed dataset:")
print(df.head())

#df.to_csv('C:\\MAIN\\it\\projects\\py\\InforceTestTask\\data\\transformed_data.csv', index=False)
output_csv_file = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_data.csv')
df.to_csv(output_csv_file, index=False)
print(f"\nTransformed data saved to '{output_csv_file}'.")
