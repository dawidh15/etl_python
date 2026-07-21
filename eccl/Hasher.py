from abc import ABC, abstractmethod
import zlib

class IHasher(ABC):
    """An interface to implement hashing algorithms."""

    # hash a dictionary where keys are pks, and values the combined data from a table
    @abstractmethod
    def hash(self,pk_combined_cols: dict):
        """
        Brief one-line summary of the function.

        Extended description of the function, explaining its purpose,
        behavior, and any important details.

        Args:
            param1 (type): Description of the first parameter.
            param2 (type): Description of the second parameter.

        Returns:
            return_type: Description of the return value.

        Raises:
            ErrorType: Explanation of the error condition.

        Examples:
            >>> result = function_name("example", 42)
            >>> print(result)
            ExpectedOutput
        """
        pass


class CRC32Hasher(IHasher):
    def hash(self, pk_combined_cols: dict):
            hashed_dict = {}
            for k, v in pk_combined_cols.items():
                # ensure string encoding before hashing
                hashed_dict[k] = zlib.crc32(v.encode())
            return hashed_dict