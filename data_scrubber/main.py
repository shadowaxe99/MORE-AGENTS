```python
import pandas as pd
from dateutil.parser import parse
from faker import Faker
from utils import load_data, save_data

def anonymize_data(df, faker):
    df['name'] = df['name'].apply(lambda x: faker.name())
    df['email'] = df['email'].apply(lambda x: faker.email())
    df['address'] = df['address'].apply(lambda x: faker.address())
    return df

def parse_dates(df):
    df['date'] = df['date'].apply(lambda x: parse(x))
    return df

def main():
    faker = Faker()
    df = load_data('data.csv')
    df = anonymize_data(df, faker)
    df = parse_dates(df)
    save_data(df, 'anonymized_data.csv')

if __name__ == "__main__":
    main()
```