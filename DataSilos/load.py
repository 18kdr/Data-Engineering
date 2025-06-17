import awswrangler as wr

def load_data_wrangler(df,path):
    wr.s3.to_parquet(df,path=f"{path}",index=False)
    print("Success")