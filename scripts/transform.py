import pandas as pd
import re
import os


INPUT_CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'data.csv')
OUTPUT_CSV_FILE = os.path.join(os.path.dirname(__file__), '..', 'data', 'transformed_data.csv')


def transform_signup_date(df):
    df['signup_date'] = pd.to_datetime(df['signup_date']).dt.strftime('%Y-%m-%d')
    return df


def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def filter_valid_emails(df):
    return df[df['email'].apply(is_valid_email)]


def extract_email_domain(df):
    df['domain'] = df['email'].apply(lambda x: x.split('@')[-1])
    return df


def main():

    df = pd.read_csv(INPUT_CSV_FILE)

    df = transform_signup_date(df)
    df = filter_valid_emails(df)
    df = extract_email_domain(df)

    print("\nTransformed dataset:")
    print(df.head())

    df.to_csv(OUTPUT_CSV_FILE, index=False)
    print(f"\nTransformed data saved to '{OUTPUT_CSV_FILE}'.")


if __name__ == "__main__":
    main()
