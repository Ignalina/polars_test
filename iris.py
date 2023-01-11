
import polars as pl

q = (
    pl.scan_csv("data/Iris.csv")
    .filter(pl.col("SepalLengthCm") > 5)
    .groupby("Species")
    .agg(pl.all().sum())
)

df = q.collect()
print(df)