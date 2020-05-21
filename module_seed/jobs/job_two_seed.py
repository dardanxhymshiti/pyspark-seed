
def process(spark, input_path, output_path, save_mode='append'):

    # read data
    df = spark.read.parquet(input_path)

    # processing
    pass

    # output
    df.write.parquet(output_path, save_mode=save_mode)



