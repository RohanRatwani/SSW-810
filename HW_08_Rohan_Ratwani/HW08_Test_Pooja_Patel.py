"""Test file"""
import unittest
from HW08_PoojaPatel import date_arithmetic, file_reader, FileAnalyzer
from datetime import datetime, timedelta
from typing import Dict,List

class Test(unittest.TestCase):
    """Test the functions"""
    def test_date_arithmetic(self):
        """ The function tests the date_airthmetic()function."""
        self.assertEqual(date_arithmetic(),(datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 241))
        self.assertNotEqual(date_arithmetic(),(datetime(2020, 3, 1, 0, 0), datetime(2019, 3, 2, 0, 0), 242))

    def test_file_reader(self):
        """The function tests the file_reader() function."""
        expected = [('123', 'Jin He', 'Computer Science'), ('234', 'Nanda Koka', 'Software Engineering'), ('345', 'Benji Cai', 'Software Engineering')]
        self.assertEqual(list(file_reader("test.txt", 3, "|", True)),expected)

class TestFileAnalyzer(unittest.TestCase):
    """ Test FileAnalyzer class"""
    def test_analyze_files(self):
        """ Test analyze_files() function."""
        file_path:FileAnalyzer = FileAnalyzer("R:\Stevens\Sem-2\SSW-810\HW_08_Rohan_Ratwani\Ronnie")
        expected:Dict[str,Dict[str,int]] = {'0_defs_in_this_file.py': {'classes': 0,'functions': 0, 'lines': 3, 'characters': 55},
            'file1.py': {'classes': 2, 'functions': 4,'lines': 25, 'characters': 270},
            'file2.py': {'classes': 2, 'functions': 5, 'lines': 20, 'characters': 205}}
        self.assertEqual(file_path.analyze_files(),expected)

if __name__ == "__main__":
    unittest.main(exit=False,verbosity=2)