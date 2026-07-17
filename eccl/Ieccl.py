"""
Interfaces for Extract Clean Conform and Load
"""
from abc import ABC, abstractmethod

class IECCLTable(ABC):
    """
    Define a interface that contains the table meta data ETLTable
	getPK -> array(columns composing the key)
	getType1 -> array
	getType2 -> array
	getType3 -> 
    """
    @abstractmethod
    def getPK(self) -> list:
        #Takes the instance and return a list with the columns that compose the PK
        pass

    @abstractmethod
    def getType1(self) -> list:
        #Takes the instance and return a list with the columns that compose the type 1 columns
        pass

    @abstractmethod
    def getType2(self) -> list:
        #Takes the instance and return a list with the columns that compose the type 2 columns
        pass

    @abstractmethod
    def getType3(self) -> list:
        #Takes the instance and return a list with the columns that compose the type 3 columns
        pass