from abc import ABC, abstractmethod
import pandas as pd

"""

"""

class ICombiner(ABC):
    # Take data, select cols_to_combine, join the values
    # then create a dict (pk: combined_values)
    @abstractmethod
    def combine(self,data: object, pk: list, cols_to_combine: list):
        pass

    # Creates a dictionary
    # first key is always "pk_combined"
    # the other keys are each of the components of the composite key
    # This data is the bases to join the composite key with the original data
    @abstractmethod
    def pk_combiner(self, data: object, pk_cols: list):
        pass

# Pandas
class PandasCombiner(ICombiner):
    def combine(self,data, pk, cols_to_combine):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Expected a pandas data frame")
        
        data["combined"] = data[cols_to_combine].astype(str).replace("nan", "").agg("".join, axis=1)
        return dict(zip(pk, data["combined"]))

    def pk_combiner(self, data, pk_cols):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("Expected a pandas data frame")
        
        data["combined_pk"] = data[pk_cols].astype(str).replace("nan", "").agg("".join, axis=1)

        pk_dict = dict()

        # call list(pd[col]) to convert to array
        pk_dict.update({"pk_combined": list(data["combined_pk"])})
        for pk_item in pk_cols:
            pk_dict.update({pk_item: list(data[pk_item])})

        return pk_dict