# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {}
# META }

# CELL ********************

secretValue=mssparkutils.credentials.getSecret('https://dp-keyvlt-dev.vault.azure.net/','Service-Principal-Id')
print("Spn :-", secretValue)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
