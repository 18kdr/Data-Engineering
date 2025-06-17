import pandera.pandas as pa

def validate_dataframe(df):
    schema = pa.DataFrameSchema(
    {
        "product_name" : pa.Column(pa.String),
        "product_price" : pa.Column(float,pa.Check.in_range(0,1000)),
        "stock_quantity" : pa.Column(float,pa.Check.in_range(0,1000), nullable = True),
        "master_id": pa.Column(pa.Int64,pa.Check.less_than_or_equal_to(3000))
    }
    )
    schema.validate(df)
    return True