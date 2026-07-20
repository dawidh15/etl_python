"""
https://code.visualstudio.com/docs/python/testing#_configure-tests

If need to reconfigure test run commnad palette (may need to close and reopen VS Code if error)
Python: Configure Test

"""
from eccl.Table import TableMetadata
import unittest



class Test_TableMetadata(unittest.TestCase):
    def setUp(self):
        self.tableMD  = TableMetadata(\
            json_path="data/table_1_definition.json"\
            ,schema_path="schema/table_schema.json"
        )

    def test_type(self):
        self.assertIsInstance(self.tableMD, TableMetadata)

    def test_pk(self):
        self.assertIsInstance(self.tableMD.pk, list)
        self.assertIsInstance(self.tableMD.pk_type, list)
        self.assertGreater(len(self.tableMD.pk),0)
        self.assertGreater(len(self.tableMD.pk_type),0)

    def test_type1(self):
        self.assertIsInstance(self.tableMD.type1, list)
        self.assertIsInstance(self.tableMD.type1_type, list)
        self.assertGreater(len(self.tableMD.type1),0)
        self.assertGreater(len(self.tableMD.type1_type),0)

    def test_type2(self):
        self.assertIsInstance(self.tableMD.type2, list)
        self.assertIsInstance(self.tableMD.type2_type, list)
        self.assertGreater(len(self.tableMD.type2),0)
        self.assertGreater(len(self.tableMD.type2_type),0)

    def test_type3(self):
        self.assertIsInstance(self.tableMD.type3, list)
        self.assertIsInstance(self.tableMD.type3_type, list)
        self.assertGreater(len(self.tableMD.type3),0)
        self.assertGreater(len(self.tableMD.type3_type),0)


if __name__ == '__main__':
    unittest.main()