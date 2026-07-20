from abc import ABC, abstractmethod
import zlib

class IHasher(ABC):

    # hash a dictionary where keys are pks, and values the combined data from a table
    @abstractmethod
    def hash(self,pk_combined_cols: dict):
        pass

"""
import zlib

def myhash(data_dict):
    hashed_dict = {}
    for k, v in data_dict.items():
        # ensure string encoding before hashing
        hashed_dict[k] = zlib.crc32(v.encode())
    return hashed_dict

"""

class CRC32Hasher(IHasher):
    def hash(self, pk_combined_cols: dict):
            hashed_dict = {}
            for k, v in pk_combined_cols.items():
                # ensure string encoding before hashing
                hashed_dict[k] = zlib.crc32(v.encode())
            return hashed_dict