"""
Interfaces for Extract Clean Conform and Load
"""
from abc import ABC, abstractmethod
import json
from jsonschema import validate
from eccl.Hasher import IHasher
from eccl.Combiner import ICombiner

class TableMetadata:
    def __init__(self, json_path: str, schema_path: str):
        self.cfg_path = json_path
        self.schema_path = schema_path

        #load table config
        table_config = self.read_json()

        # Load info to object
        self.name = table_config.get("table_name")
        self.pk = []
        for pk_item in table_config.get("PK"):
            self.pk.append(pk_item[0])

        self.pk_type = []
        for pk_item in table_config.get("PK"):
            self.pk_type.append(pk_item[1])

        self.type1 = []
        for type1_item in table_config.get("Type 1"):
            self.type1.append(type1_item[0])

        self.type1_type = []
        for type1_item in table_config.get("Type 1"):
            self.type1_type.append(type1_item[1])
        
        self.type2 = []
        for type2_item in table_config.get("Type 2"):
            self.type2.append(type2_item[0])

        self.type2_type = []
        for type2_item in table_config.get("Type 2"):
            self.type2_type.append(type2_item[1])

        self.type3 = []
        for type3_item in table_config.get("Type 3"):
            self.type3.append(type3_item[0])

        self.type3_type = []
        for type3_item in table_config.get("Type 3"):
            self.type3_type.append(type3_item[1])


    def read_json(self) -> str:
        #raise NotImplementedError("Method not Implemented.")
        # Load table spec
        with open(self.cfg_path, mode="r", encoding="utf-8") as table_config:
            data = json.load(table_config)
        
        # Load schema
        with open(self.schema_path, mode="r", encoding="utf-8") as table_schema:
            schema = json.load(table_schema)

        # Validate json conforms to the schema
        try:
            validate(instance=data, schema=schema)
            return data
        except Exception as e:
            print(e)    


class Table():
    table_metadata: TableMetadata
    pk_data: dict #map a combined pk to the composite keys for later joining
    pk_hash: dict
    type1_hash: dict
    type2_hash: dict
    type3_hash: dict
    hasher: IHasher
    combiner: ICombiner

    # Combiner can be set at construction or later
    def __init__(self, metadata: TableMetadata, combiner: ICombiner, hasher: IHasher, data: object):
        self.table_metadata = metadata
        self.combiner = combiner
        self.hasher = hasher

        # Calculate PK dict first, This is a dictionary with the combined pk
        # plus the original composite keys.
        # Returns the data needed to join the composite key to the table if needed
        self.pk_data = self.combiner.pk_combiner(data = data, pk_cols = self.table_metadata.pk)
        
        # Combine records, apply hash and store.
        t1dic = self.use_combiner(data=data\
                                  ,pk = self.pk_data.get("pk_combined")\
                                  , cols_to_combine= self.table_metadata.type1
                                )
        self.type1_hash = self.__use_hasher(t1dic)
        del t1dic

        t2dic = self.use_combiner(data=data\
                                  ,pk = self.pk_data.get("pk_combined")\
                                  , cols_to_combine= self.table_metadata.type2
                                )
        self.type2_hash = self.__use_hasher(t2dic)
        del t2dic

        t3dic = self.use_combiner(data=data\
                                  ,pk = self.pk_data.get("pk_combined")\
                                  , cols_to_combine= self.table_metadata.type3
                                )
        self.type3_hash = self.__use_hasher(t3dic)
        del t3dic

    #Strategy pattern
    # Hasher can be set at runtime
    def set_hasher(self, new_hasher: IHasher):
        self.hasher = new_hasher

    # Private
    # It'll be used to initialize types 1 to 3
    def __use_hasher(self, pk_combined_cols: dict):
        return self.hasher.hash(pk_combined_cols)
    
    # Set combiner
    def set_combiner(self, new_combiner: ICombiner):
        self.combiner = new_combiner

    def use_combiner(self, data: object, pk: list, cols_to_combine: list):
        return self.combiner.combine(data, pk, cols_to_combine)

    # Take metadata from table and initialize object