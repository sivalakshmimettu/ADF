# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "4d9c7c6d-0648-45ab-9a15-4539ad62a97a",
# META       "default_lakehouse_name": "LH_CREATETABLES",
# META       "default_lakehouse_workspace_id": "fb139938-22c6-402c-bac3-752ec11906f3",
# META       "known_lakehouses": [
# META         {
# META           "id": "4d9c7c6d-0648-45ab-9a15-4539ad62a97a"
# META         },
# META         {
# META           "id": "1c978bb3-e933-48cc-85c9-0ef5ff4e0cb6"
# META         }
# META       ]
# META     }
# META   }
# META }

# CELL ********************

from pyspark.sql import SparkSession

# Create a Spark session (if not created automatically)
spark = SparkSession.builder.getOrCreate()

# Define the schema and create a Delta table
df = spark.createDataFrame([], "Description string, Id string, Type string, Code string,CreatedBy string, CreatedOn string, ModifiedBy string, ModifiedOn string, RecordIngestedBy string, RecordIngestedOn TIMESTAMP, RecordModifiedBy string, RecordModifiedOn TIMESTAMP, RecordStatus INT")

# Write as Delta table in Lakehouse folder
df.write.format("delta").save("Tables/ReferenceCode")  # Saving as a Delta table in the Lakehouse folder


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC create table LH_ConceptOne.DateCalender(Date String, DateKey String, DayInQuarter String, DayName String, DayNameAbbrevation String, DayOfMonth String, DayOfWeek String, DayOfWeekInMonth String, DayOfYear String, FirstDayOfMonth String, FirstDayOfQuarter String, FirstDayofYear String, Holiday String, IsHoliday String, IsWeekday String, IsWeekend String, LastDayOfQuarter String, LastDayofMonth String, LastDayofYear String, Month String, MonthAbbrevation String, MonthName String, MonthOfQuarter String, Quarter String, QuarterName String, QuarterShortName String, WeekOfMonth String, WeekOfQuarter String, WeekOfYear String, YYYYMM String, Year String, YearAndQuarter String, YearMonth String, YearName String, FirstDayOfFiscalYear String, FiscalDateKey String, FiscalDayOfYear String, FiscalMonth String, FiscalQuarter String, FiscalQuarterName String, FiscalWeekOfYear String, FiscalYear String, IsFirstDayOfFiscalYear String, IsLastOfFiscalYear String, LastDayOfFiscalYear String, Century String, CreatedBy String, CreatedOn String, ModifiedBy String, ModifiedOn String, RecordIngestedBy string, RecordIngestedOn timestamp, RecordModifiedBy string, RecordModifiedOn timestamp, RecordStatus integer)"
# MAGIC   

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC create table LH_ConceptOne.ReferenceCode(Description string, Id string, Type string, Code string,CreatedBy string, CreatedOn string, ModifiedBy string, ModifiedOn string, RecordIngestedBy string, RecordIngestedOn TIMESTAMP, RecordModifiedBy string, RecordModifiedOn TIMESTAMP, RecordStatus INT)

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************

# MAGIC %%sql
# MAGIC create table LH_CREATETABLES.address as 
# MAGIC SELECT * FROM LH_ConceptOne.address;

# METADATA ********************

# META {
# META   "language": "sparksql",
# META   "language_group": "synapse_pyspark"
# META }

# CELL ********************


# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
