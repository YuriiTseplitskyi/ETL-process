import pandas as pd
import re
from config.constants import INPUT_CSV_FILE, TRANSFORMED_CSV_FILE


def transform_signup_date(df: pd.DataFrame) -> pd.DataFrame:
    df['signup_date'] = pd.to_datetime(df['signup_date']).dt.strftime('%Y-%m-%d')
    return df


def is_valid_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None


def filter_valid_emails(df: pd.DataFrame) -> pd.DataFrame:
    return df[df['email'].apply(is_valid_email)]


def extract_email_domain(df: pd.DataFrame) -> pd.DataFrame:
    df['domain'] = df['email'].apply(lambda x: x.split('@')[-1])
    return df


def main():

    df = pd.read_csv(INPUT_CSV_FILE)

    df = transform_signup_date(df)
    df = filter_valid_emails(df)
    df = extract_email_domain(df)

    print("\nTransformed dataset:")
    print(df.head())

    df.to_csv(TRANSFORMED_CSV_FILE, index=False)
    print(f"\nTransformed data saved to '{TRANSFORMED_CSV_FILE}'.")


if __name__ == "__main__":
    main()
