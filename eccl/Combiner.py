from abc import ABC, abstractmethod
import pandas as pd

class ICombiner(ABC):
    """Create dictionaries for IHasher."""
    @abstractmethod
    def combine(self,data: object, pk: list, cols_to_combine: list):
        """
        Takes data from a specific implementation, select cols_to_combine, join the values and then create a dict (pk: combined_values)

        Args:
            self (ICombiner): It needs an instance of a Combiner.
            data (object): A data frame like object (tables and records). Depends on the implementation.
            pk (list): the output of Table.pk_data.get("pk_combined").
            cols_to_comine (list): A list of columns to combine. Usually `Table.table_metadata.type<1:3>`.

        Returns:
            return_type: a dictionary to use as input in `IHasher.hash()`

        Raises:
            TypeError: For the specific implementation, fails if *data* is not the right object type.

        Examples:
            >>> result = ICombiner.combiner(data, pk_list, col_list)
            >>> #print(result)
            a dictionary
        """
        pass

    @abstractmethod
    def pk_combiner(self, data: object, pk_cols: list):
        """
        Takes data from a specific implementation and combines the values of the primary key then create a dict (pk_combined: list(composite key elements))

        Args:
            self (ICombiner): It needs an instance of a Combiner.
            data (object): A data frame like object (tables and records). Depends on the implementation.
            pk_cols (list): the output of `self.table_metadata.pk`.

        Returns:
            return_type: a dictionary to use as input in `ICombiner.combine()`

        Raises:
            TypeError: For the specific implementation, fails if *data* is not the right object type.

        Examples:
            >>> result = ICombiner.pk_combiner(data, pk_cols)
            >>> #print(result)
            [{"1ax": [1,"a","x"], "2by": [2,"b","y"]} 
        """
        pass

# Pandas
class PandasCombiner(ICombiner):
    """Create dictionaries for IHasher taking a pandas dataframe as the data argument."""
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