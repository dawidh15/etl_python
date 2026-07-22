from abc import ABC, abstractmethod
import zlib

class IHasher(ABC):
    """An interface to implement hashing algorithms."""

    
    @abstractmethod
    def hash(self,pk_combined_cols: dict):
        """
        Hash a dictionary where keys are pks, and values the combined data from a table

        `pk_combined_columns` is the output of a *Combiner*. It's a dictionary and thus, it's agnostic of the original data source format. Mainly called internally from another methods.

        Args:
            self (object): It needs an instance of a Hasher.
            pk_combined_cols (dict): The output of a *Combiner*

        Returns:
            return_type: another dictionary with the combined primary keys as dictionary keys, and the hashed values as dictionary values.

        Raises:
            ErrorType: Read the actual implementation details.

        Examples:
            >>> result = IHasher.hash(pk_combined_cols)
            >>> #print(result)
            a dictionary
        """
        pass


class CRC32Hasher(IHasher):
    """Basic implementation of crc32 hashing algorithm from **zlib** module."""
    def hash(self, pk_combined_cols: dict):
            hashed_dict = {}
            for k, v in pk_combined_cols.items():
                # ensure string encoding before hashing
                hashed_dict[k] = zlib.crc32(v.encode())
            return hashed_dict