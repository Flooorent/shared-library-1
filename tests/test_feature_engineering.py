from pyspark.sql import SparkSession
from shared_library_1.feature_engineering import sum_cols


def test_sum_cols():
    spark = SparkSession.builder.getOrCreate()

    df = spark.createDataFrame([[2.8, 3.1], [0.0, 20.2]]).toDF("x", "y")
    actual_df = sum_cols(df, "x", "y")

    expected_df = spark.createDataFrame(
        [
            [2.8, 3.1, 5.9],
            [0.0, 20.2, 20.2],
        ]
    ).toDF("x", "y", "sum_x_y")

    assert actual_df.collect() == expected_df.collect()
