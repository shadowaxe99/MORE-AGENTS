```python
import pandas as pd
from faker import Faker
from dateutil.parser import parse

def anonymize_data(df):
    faker = Faker()
    df['name'] = df['name'].apply(lambda x: faker.name())
    df['email'] = df['email'].apply(lambda x: faker.email())
    df['address'] = df['address'].apply(lambda x: faker.address())
    return df

def parse_dates(df, date_columns):
    for col in date_columns:
        df[col] = df[col].apply(lambda x: parse(x))
    return df

def scrub_data(df, date_columns):
    df = anonymize_data(df)
    df = parse_dates(df, date_columns)
    return df
```