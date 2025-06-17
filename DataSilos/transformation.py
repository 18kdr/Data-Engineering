import pandas as pd

#Drop the columns function
def drop_columns(df, columns):
    return df.drop(columns, axis=1, inplace=True)

def strip_columns(df, columns):
    for column in columns:
        if column in df.columns:
            df[column] = df[column].str.strip()
    return df

def split_columns(df, column, coluumnName1, columnName2, seperator, splits):
    if column in df.columns:
        df[[coluumnName1,columnName2]] = df[column].str.split(f'{seperator}', n=splits, expand=True)
    return df
    
def fill_missing_values(df):
    df.fillna({
    "product_sub_category": "unknown",
    "product_description" : "unknown",
    "product_price" : df['product_price'].median()
    }, inplace = True)
    return df