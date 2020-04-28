""" HW08 implementation file layout template"""
from datetime import datetime, timedelta
from typing import Tuple, List, Iterator,Dict



def date_arithmetic() -> Tuple[datetime, datetime, int]:
    """ Your docstring should go here for the description of the function."""
    date1: datetime = "Feb 27, 2020"
    date2: datetime = "Feb 27, 2019"
    date3: datetime = "Sep 30, 2019"
    dt1: datetime = datetime.strptime(date1, "%b %d, %Y")
    dt2: datetime = datetime.strptime(date2, "%b %d, %Y")
    dt3: datetime = datetime.strptime(date3, "%b %d, %Y")
    num_days: int = 3
    three_days_after_02272000: datetime = dt1 + timedelta(days=num_days)
    three_days_after_02272017: datetime = dt2 + timedelta(days=num_days)
    days_passed_01012017_10312017: int = dt3 - dt2
    print(three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017)

    return three_days_after_02272000, three_days_after_02272017, days_passed_01012017_10312017


def file_reader(path, fields, sep=',', header=False) -> Iterator[Tuple[str]]:
    """ Your docstring should go here for the description of the function."""
    try:
        fp = open(path, "r")
    except FileNotFoundError:
        print("File not found")
    else:
        with fp:
            cwid: str = 0
            name: str = ""
            major: str = ""
            next(fp)
            for line in fp:
                item = tuple(line.split("|"))
                print(item)
                # yield item


class FileAnalyzer:
    """ Your docstring should go here for the description of the class."""

    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory  # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()

        self.analyze_files()  # summerize the python files data

    def analyze_files(self) -> None:
        """ Your docstring should go here for the description of the method."""
        pass  # implement your code here

    def pretty_print(self) -> None:
        """ Your docstring should go here for the description of the method."""


date_arithmetic()
file_reader("func2_test.txt", "|")

# for item in file_reader("student_majors.txt.rtf","|"):
#     print(item)

