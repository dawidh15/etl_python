"""
install pipreqs to scan code and determine used dependencies
PS> pip install pipreqs

creates a requirements.txt
PS> pipreqs .--force

pip install mkdocs mkdocs-material "mkdocstrings[python]"
# Create templates
mkdocs new

build local
mkdocs serve

build docs
mkdows build
"""


import pandas as pd
from eccl.Table import TableMetadata, Table
from eccl.Combiner import PandasCombiner
from eccl.Hasher import CRC32Hasher

data = pd.read_csv("data/sample_data.csv",  encoding="utf-8")

#read Metadata
metadata = TableMetadata(json_path="data/table_1_definition.json",schema_path="schema/table_schema.json")

#Initiate instance combiner
pd_combiner = PandasCombiner()
crc32_hasher = CRC32Hasher()

# Create table object with metadata
# set combiner and hasher at runtime!!
myTable = Table(metadata=metadata, combiner=pd_combiner, hasher=crc32_hasher, data=data)

# combiner can be changed
#myTable.set_combiner(new_combiner=pd_combiner)
