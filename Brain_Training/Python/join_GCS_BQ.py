import bigframes.pandas as bpd
from google.cloud import bigquery
import pandas as pd

# set the GCP project id and for bucket, the location id
bpd.options.bigquery.project = "deeplearningproject-472318"
bpd.options.bigquery.location = "us-east1"

# Load directly into a local Pandas DataFrame (handle missing files)
ratecode_df = None
taxizone_df = None

# 1. Read the BigQuery table
bq_df = bpd.read_gbq("deeplearningproject-472318.python_df.Trip_Data")

# 2. Read the GCS file (CSV, Parquet, etc.)
# BigFrames processes this as an external table automatically
try:
	ratecode_df = bpd.read_csv("gs://deep_python_df_test/RateCodes.csv")
	print(ratecode_df.head(1))
except FileNotFoundError:
	print("Warning: RateCodes.csv not found in GCS; continuing without it.")
except Exception as e:
	print(f"Warning: could not read RateCodes.csv: {e}")

try:
	taxizone_df = bpd.read_csv("gs://deep_python_df_test/TaxiZones.csv")
except FileNotFoundError:
	print("Warning: TaxZones.csv not found in GCS; continuing without it.")
except Exception as e:
	print(f"Warning: could not read TaxZones.csv: {e}")


final_df = bq_df.join(ratecode_df, on="RatecodeID", how="inner")
# print(final_df.head(1))

# 3. Join the datasets
# This execution is pushed down to BigQuery's engine
# Preview or save the result back to BigQuery

final_df.to_gbq("your-project.your_dataset.final_set")


# client = bigquery.Client(project="deeplearningproject-472318")
#
# query = "SELECT  tpep_pickup_datetime FROM `deeplearningproject-472318.python_df.Trip_Data` where 1=1 and  format_date ('%B', tpep_pickup_datetime)='January' limit 7"
#
# trip_data_df = client.query(query).to_dataframe()
#
# print(trip_data_df.head(1))