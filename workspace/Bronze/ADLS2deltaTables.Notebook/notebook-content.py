# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "1c978bb3-e933-48cc-85c9-0ef5ff4e0cb6",
# META       "default_lakehouse_name": "LH_ConceptOne",
# META       "default_lakehouse_workspace_id": "fb139938-22c6-402c-bac3-752ec11906f3",
# META       "known_lakehouses": [
# META         {
# META           "id": "1c978bb3-e933-48cc-85c9-0ef5ff4e0cb6"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format('Parquet').load("abfss://Insurance@onelake.dfs.fabric.microsoft.com/LH_ConceptOne.Lakehouse/Files/Raw/Raw/PolicyAdmin/SRC_ConceptOne/Address/2025/03/24/15")
print(df.count())

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

from delta.tables import DeltaTable
from pyspark.sql.functions import col

# Read the source Parquet data
df = spark.read.format("parquet").load("abfss://Insurance@onelake.dfs.fabric.microsoft.com/LH_ConceptOne.Lakehouse/Files/Raw/Raw/PolicyAdmin/SRC_ConceptOne/Address/2025/03/24/14")

# Define the Delta table path
delta_table_path = "abfss://Insurance@onelake.dfs.fabric.microsoft.com/LH_ConceptOne.Lakehouse/Tables/Delta/Address_001"

# Define the list of Primary Key columns
pk_columns = ["Entity_ID", "Address_Type","Address_ID"]  # Replace with actual PK columns

# Check if the Delta table exists
if DeltaTable.isDeltaTable(spark, delta_table_path):
    # Load the existing Delta table
    delta_table = DeltaTable.forPath(spark, delta_table_path)

    # Construct the merge condition dynamically for multiple PKs
    merge_condition = " AND ".join([f"target.{col} = source.{col}" for col in pk_columns])

    # Get all columns except PK columns for updates
    update_columns = [col for col in df.columns if col not in pk_columns]

    # Build dynamic update dictionary
    update_dict = {col_name: col(f"source.{col_name}") for col_name in update_columns}

    # Perform merge operation
    delta_table.alias("target").merge(
        df.alias("source"),
        merge_condition
    ).whenMatchedUpdate(set=update_dict
    ).whenNotMatchedInsert(values={col_name: col(f"source.{col_name}") for col_name in df.columns}
    ).execute()
    
else:
    # If the Delta table doesn't exist, create it by writing the DataFrame as a new Delta table
    df.write.format("delta").mode("overwrite").save(delta_table_path)

print("Merge operation completed successfully.")


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

df = spark.read.format('Parquet').load("abfss://Insurance@onelake.dfs.fabric.microsoft.com/LH_ConceptOne.Lakehouse/Tables/Delta/Address_001")
print(df.schema)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
