from os.path import join as join_path


def process(spark, input_path, output_path, save_mode='append'):

    # read data
    df = spark.read.parquet(input_path)

    # processing
    pass

    # output
    store_processed_data_path = join_path('s3://', output_path)
    df.write.parquet(store_processed_data_path, save_mode=save_mode)



