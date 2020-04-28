import unittest
from HW08_Heli_Patel import date_arithmetic,file_reader,FileAnalyzer
from datetime import datetime, timedelta
from typing import Dict,List,Tuple

class datetestclass(unittest.TestCase):

    def test_date_arithmetic(self):
        """"Testing date and time function"""

        self.assertEqual(date_arithmetic(), (datetime(2020,3,1,0,0), datetime(2019,3,2,0,0),241))
        self.assertNotEqual(date_arithmetic(), (datetime(2020,3,1,0,0), datetime(2019,3,2,0,0),0))
    
    def test_analyze_files(self):
        """Testing the python file and counting of the classes,functions,lines,characters from python file."""
        f:FileAnalyzer=FileAnalyzer("R:\Stevens\Sem-2\SSW-810\HW_08_Rohan_Ratwani\Ronnie")
        output: Dict = {'0_defs_in_this_file.py': {'classes': 0, 'functions': 0, 'lines': 3, 'chars': 55},  'file1.py': {'classes': 2, 'functions': 4, 'lines': 25, 'chars': 270}, 'file2.py': {'classes': 2, 'functions': 5, 'lines': 20, 'chars': 205}}
        self.assertEqual(f.analyze_files(), output)

    def test_file_reader(self):
        """Testing the text file and reading of the file and raising the Error. """
        print(list(file_reader("func2_test.txt", 3, '|', True)))
        operated: List[Tuple] = [('123', 'Jin He', 'Computer Science'),('234', 'Nanda Koka', 'Software Engineering'),('345', 'Benji Cai', 'Software Engineering')]
        self.assertEqual(list(file_reader("func2_test.txt", 3, '|', True)), operated)

    p = open("func2_test.txt", 'r')
    for line in p:
        print(line)

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
