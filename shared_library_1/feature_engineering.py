from pyspark.sql import functions as F


def sum_cols(df, col1, col2):
    return df.withColumn(f"sum_{col1}_{col2}", F.col(col1) + F.col(col2))
