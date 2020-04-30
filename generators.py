from typing import List,Dict,Tuple,DefaultDict
from collections import Counter,defaultdict
import random, string, os,sys
from typing import Iterator,Optional,Any,Sequence
from datetime import datetime, timedelta

# def generator_function() -> List[int]:
#     generator_list:List[int] = [[1,2,3],[4,5,6],[7,8,9]]
#     for item in generator_list:
#         yield item

# def call_generator():
#     print(generator_function())
#     for i in generator_function():
#         print(i)
#     return [[1,2,3],[4,5,6],[7,8,9]]
    

# call_generator()

# assert call_generator() == [[1,2,3],[4,5,6],[7,8,9]]


# """" magic methods"""

# class Magic:
#     def __init__(self,string: str) -> None:
#         self.string = string

#     def __add__(self,other: str) -> str:
#         return self.string + other 
    
# if __name__ == "__main__":
#     magic = Magic("Pooja")
#     full_name = magic + "  Patel"
#     print(f"My full name is: {full_name}")


# """ Example 2 Magic Method """

# class Fraction:
#     def __init__(self,numerator: int, denominator: int) -> None:
#         self.numerator = numerator
#         self.denominator = denominator
    
#     def __str__(self) -> str:
#         return f"{self.numerator}\{self.denominator}"

#     def operation(self, operator: str, other: "Fraction") -> "Fractions":
#         if operator == '+':
#             num = (self.numerator * other.denominator) + (other.denominator * self.numerator)
#             denom = (self.denominator * other.denominator)
#             return Fraction(num, denom)

# def ask_user():
#     num = int(input("Enter numerator: "))
#     denom = int(input("Enter Denominator: "))
    
#     return Fraction(num, denom)

# def main():

#     f1 = ask_user()
#     f2 = ask_user()

#     operation = input("operation: ")

#     print(f1.operation(operation,f2))

    

# main()




# """ lambda Example """
# z:Dict = {"Pooja":"Patel","Rohan":"Ratwani"}
# x = [(a+b) for a,b in z.items()]
# print(x)

# x = lambda a,b: a + b
# print(x(3,4))
#sorted(current.children, key = lambda x:individuals[x].birth if individuals[x].birth else datetime.now() if current.children else 'NA')


# dict1: Dict[str,List[str]] = {"A": [1,2,3,4], "B": [3,4,5,6,7]}
# list1 = [("a",1),("b",2),("c",3)]
# list2 = [1,2,3,3,4,5,6,7,7]
# l=[]
# print([l.append(item) for k,v in dict1.items() for item in v if item not in l ])


# d = { k:v for k,v in list1}
# s = {k for k,v in list1}
# print(d)
# print(l)
# print(s)

# def tuple_func() -> Tuple[str]:
#     return (1,5,6)
# a,b,c = tuple_func()
# print(a,b,c)

# x = ["Guru99", 20, "Education"]   # tuple packing
# [company, emp, profile] = x    # tuple unpacking
# print(company)
# print(emp)
# print(profile)

# mystr="My name is Pooja Yeddi Pooja"

# counter1 = Counter(mystr.split())
# print(counter1)

# list2 = [1,2,3,3,4,5,6,7,7]
# a = list2.remove(1)
# print(a)
''' memoization '''
# def memoize(func):
#     cache = dict()

#     def memoized_func(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result

#     return memoized_func

# factorial_memo = {2:2}
# def factorial(k):
#     if k < 2: return 1
#     if k not in factorial_memo:
#         print(k)
#         print(factorial(k-1))
#         factorial_memo[k] = k * factorial(k-1)
#     return factorial_memo[k]

# print(factorial(3))

""" parameters """

# def foo(x, use_max=False, values = [3,10]):
#     #print(use_max)
#     return x + (min(values) if use_max else max(values))

# print(foo(1))

""" Kwargs """

# def my_func(**kwargs):
#     for key, value in kwargs.items():
#         print(f" key: {key} value: {value}")

# z:Dict = {"Pooja":"Patel","Rohan":"Ratwani"}
# my_func(**z)


""" generators """

# def random_integer_generator(minimum: int, maximum: int) -> Iterator[int]:

#     while True:
#         r = random.randint(minimum,maximum)
#         yield r

# # i = random_integer_generator(10,20)
# # print(next(i))

# def find_target(target, min_value, max_value, max_attempts) -> Optional[int]:
#     maximum = 0
#     random_count = 0
#     while maximum <= max_attempts:
#         maximum += 1
#         for i in random_integer_generator(min_value,max_value):
#             random_num = i
#             random_count += 1
#             if random_num == target:
#                 return random_count

# print(find_target(3,3,3,1))

# a = sum(range(2,9))
# print(a)

"""Enumerate"""
# mystr = "Pooja Patel is my Bestest Friendddddd!!!!!!!"

# for k,v in enumerate(mystr.split()):
#     print(k,v)

# for k,v in enumerate({1:'one',2:'two',3:'three'}):
#      print(k,v)

# """Zip"""
# seq1 = range(0,3)
# seq2 = [3,4,5,6]
# sequences=seq1, seq2
# print(list(zip(*sequences)))

# """*args"""

# def demo_args(*args):
#     for item in args:
#         print(item)

# demo_args([1,2,4],"A",1)




""" yield """

# def gen(n: int) -> Iterator[int]:
#     print("gen function called")
#     yield from range(n)
#     print("gen function called 2")
#     yield from range(n,-1,-1)

# for item in gen(2):
#     print(item)

"""HW-4"""

"Part-1"
# def count_vowels(s: str) -> int:
#     dict1: Dict(int) = {'a':0,'e':0,'i':0,'o':0,'u':0,}
#     stri = "Hello"
#     for i in s.lower():
#         if i in dict1.keys():
#             dict1[i] += 1
#       # Your definition goes here
#     print(sum(dict1.values()))
#
# count_vowels("HEllo")
# count_vowels("WORLD")
# count_vowels("hello")

"(b)"
# def count_vowels(s: str) -> int:
#     dict1: Dict(int) = {'a':0,'e':0,'i':0,'o':0,'u':0,}
#     # return len([i for i in s.lower() if i in ['a','e','i','o','u']])
#     return sum(({x: sum(x.count(y) for y in dict1.keys()) for x in s.lower()}).values())
#
#
# print(count_vowels("HEllo"))
# print(count_vowels("WORLD"))
# print(count_vowels("hello"))



"Part-2"
"(a)"
# def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
#     l:List = []
#     if target not in sequence:
#         print (None)
#     for offset,item in enumerate(sequence):
#         if item == target:
#             l.append(offset)
#     print (l[-1])
#
# last_occurrence(33,[ 42, 33, 21, 33,44,33, 66, 33 ])

"(b)"
# def last_occurrence(target: Any, sequence: Sequence[Any]) -> Optional[int]:
#     return max([offset for offset,item in enumerate(sequence) if item == target ])
#
# print(last_occurrence(33,[ 42, 33, 21, 33,44,33, 66, 33 ]))


"Part-3"
def fraction_simplify(numerator,denominator):
    num = abs(numerator)
    denom = abs(denominator)
    n:int = 0
    d:int = 0
    a:str = ""
    i=1
    gcf:int = 0

    try:
        if denom == 0:
            raise ZeroDivisionError("ZeroDivisionError: Denominator can't be 0")

    except ZeroDivisionError as ze:
        print(ze)

    else:
        while (i<=num and i<=denom):
            if num % i == 0 and denom % i == 0:
                gcf = i
                n = int(num / gcf)
                d = int(denom / gcf)
            i += 1
        print (f"Simplified Fraction is : {n}/{d}")

fraction_simplify(-8,12)
fraction_simplify(1,3)
fraction_simplify(1,0)

"Part-4"
# def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
#     lst:List = []
#     def enum_gen():
#         for i in range(len(seq)):
#             yield i,seq[i]
#
#     for item in enum_gen():
#         print(item)
#
# my_enumerate("Hello, World!")
# my_enumerate([1,2,3,4,5,6,7,8,9,10])

"""--------------------HomeWork-5----------------------"""

"--Part-1--"
# def reverse(s: str) -> str:
#     rev:str = ""
#     for i in s:
#         rev = i + rev
#     return rev
#
# print(reverse("ROHAN"))

"--Part-2--"
# def substring(target: str, s: str) -> int:
#     if target in s:
#         for i in range(len(s)):
#             if target == s[i:i+len(target)]:
#                 print(i)
#     else:
#         print(-1)
#
# substring("he","hello")
# substring("ello","hello")
# substring("xxx","hello")
# substring("ho","holloh")

# def find_second(target: str, string: str) -> int:
#     offset = string.find(target)
#     return string.find(target, offset + 1)
#
# print(find_second('iss','Mississippi'))

"--Part-4--"

def get_lines(path: str) -> Iterator[str]:
    file_name = os.path.join(path)
    try:
        fp: IO = open(file_name)
    except FileNotFoundError:
        print("File not found")
    else:
        with fp:
            for line in fp:
                line = line.rstrip("\n")
                while line.endswith("\\"):
                    line = line[:line.find('\\')]
                    line = line + next(fp).strip('\n')
                if line.startswith("#"):
                    continue
                else:
                    for item in line:
                        if item == "#":
                            line1 = line.split("#")
                            yield line1[0]
                            break
                    else:
                        yield line

#get_lines("HW_5_part_4_test.txt")
for item in get_lines("HW_5_part_4_test.txt"):
    print((item))

"""--------------------HomeWork-6----------------------"""

"--Part-1--"

# def list_copy(l: List[Any]) -> List[Any]:
#     return [item for item in l]
# print(list_copy([1,2,3,4,5]))

"--Part-2"

# def list_intersect(l1: List[Any], l2: List[Any]) -> List[Any]:
#     return [x for x in set(l1).intersection(set(l2))]
#
# print(list_intersect([1,2,5,6,3],[3,2,1,4,7]))

"--Part-3--"

# def list_difference(l1: List[Any], l2: List[Any]) -> List[Any]:
#     return [ item for item in set(l1).difference(set(l2))]
#
# print(list_difference([1,2,5,6,3],[3,2,1,4,7]))

"--Part-4--"
#
# def remove_vowels(string: str) -> str:
#     vowels = 'a','e','i','o','u','A','E','I','O','U'
#     return (" ".join([item for item in string.split(" ") if not item.startswith(vowels)]))
#
# print(remove_vowels("I am Rohan Ratwani"))
# print(remove_vowels("Rohan Ratwani A a"))

"--Part-5--"

# def check_pwd(password: str) -> bool:
#     p = list(password)
#     if p[0].isdigit() and len([x for x in p if x.isupper()])>=2 and len([x for x in p if x.islower()])>=1:
#         return True
#     else:
#         return False
# print(check_pwd("1HHello"))
# print(check_pwd("Hello"))

"""--------------------HomeWork-7----------------------"""

"--Part-1.1--"
def anagrams_lst(str1, str2):
    return True if sorted(str1.lower()) == sorted(str2.lower()) else False
    #return True if len([(x,y)for x in list(str1.lower()) for y in list(str2.lower())]) == len(str1) else False
    # if len([(x,y)for x in list(str1.lower()) for y in list(str2.lower()) if Counter(x) == Counter(y)]) == len(str1):
    #     return True
    # else:
    #     False

print(anagrams_lst("cinema","iceman"))
# print(anagrams_lst("dormitory","dirtyroom"))
# print(anagrams_lst("hello","Rohan"))

"--Part-1.2--"
# def anagrams_dd(str1: str, str2: str) -> bool:
#     dd:DefaultDict = defaultdict(int)
#     for ch in str1.lower():
#         dd[ch]+=1
#     for c in str2.lower():
#         if c in dd.keys():
#             dd[c] -= 1
#         else:
#             return False
#     for j in dd.values():
#         if j == 0:
#             return True
#         else:
#             return False
#
# print(anagrams_dd("cinema","iceman"))
# print(anagrams_dd("dormitory","dirtyroom"))
# print(anagrams_dd("hello","Rohan"))
# print(anagrams_dd("NAHOR","Rohan"))

"--Part-1.3--"
# def anagrams_cntr(str1, str2):
#     return True if Counter(str1.lower()) == Counter(str2.lower()) else False
#
# print(anagrams_cntr("cinema","iceman"))
# print(anagrams_cntr("dormitory","dirtyroom"))
# print(anagrams_cntr("hello","Rohan"))
# print(anagrams_cntr("NAHOR","Rohan"))

"--Part-2--"
# def covers_alphabet(sentence: str) -> bool:
#     return True if set(sentence.lower()).intersection(set(string.ascii_lowercase[0:])) == set(string.ascii_lowercase[0:]) else False
#
# print(covers_alphabet("AbCdefghiJklomnopqrStuvwxyz"))
# print(covers_alphabet("The' ?quick, brown, fox; jumps over the lazy dog!"))
# print(covers_alphabet("xyz"))

'--Part-3--'
# def web_analyzer(weblogs: List[Tuple[str, str]]) -> List[Tuple[str, List[str]]]:
#     lst:List = []
#     dd:DefaultDict()= defaultdict(set)
#     [dd[j].add(i) for i,j in weblogs]
#     [lst.append((key,list(sorted(value)))) for key, value in dd.items()]
#     return sorted(lst)
#
# weblogs: List[Tuple[str, str]] = [
#      ('Nanda', 'google.com'), ('Maha', 'google.com'),
#      ('Fei', 'python.org'), ('Maha', 'google.com'),
#      ('Fei', 'python.org'), ('Nanda', 'python.org'),
#      ('Fei', 'dzone.com'), ('Nanda', 'google.com'),
#      ('Maha', 'google.com'), ('Rohan','google.com'), ('Pooja','google.com') ]
#
# print(web_analyzer(weblogs))

"""--------------------HomeWork-8----------------------"""

"--Part-1--"

# def date_arithmetic()-> Tuple[datetime, datetime, int]:
#     """ Code segment demonstrating expected return values. """
#     date1: str = "27 Feb 2020"
#     date2: str = "27 Feb 2019"
#     date3: str = "01 Feb 2019"
#     date4: str = "30 Sep 2019"
#     three_days_after_02272020: datetime =  datetime.strptime(date1,"%d %b %Y") + timedelta(days=3)# your code goes here for calculation
#     three_days_after_02272019: datetime =  datetime.strptime(date2,"%d %b %Y") + timedelta(days=3)# your code goes here for calculation
#     days_passed_02012019_09302019: int =  (datetime.strptime(date4,"%d %b %Y")-datetime.strptime(date3, "%d %b %Y")).days# your code goes here for calculation
#
#     return three_days_after_02272020, three_days_after_02272019, days_passed_02012019_09302019
#
# print(date_arithmetic())

"--Part-3--"

class FileAnalyzer:

    def __init__(self, directory: str) -> None:
        """ Your docstring should go here for the description of the method."""
        self.directory: str = directory # NOT mandatory!
        self.files_summary: Dict[str, Dict[str, int]] = dict()
        self.analyze_files()  # summerize the python files data

    def analyze_files(self) -> None:
            """ Your docstring should go here for the description of the method."""
            pass  # implement your code here

    def pretty_print(self) -> None:
            """ Your docstring should go here for the description of the method."""
            pass  # implement your code here

"""--------------------HomeWork-2----------------------"""

"--Question-2--: FRACTIONS"
# class Fraction:
#     def __init__(self):
#
#         self.numerator:int = numerator
#         self.denominator:int = denominator
#         self.operator:int = operator
#         if self.denominator == 0:
#             raise ZeroDivisionError("Denominator can not be 0!!")
#
#     def __str__(self):
#         return f"{self.numerator}/{self.denominator}"
#
#     #def operations()
#     def main():
#
# if __name__ == '__main__':
#     main()

l = [(1,2),(3,4)]
# for k,v in l:
#     print(k,v)
l = [1,2,3,4,5,3,2]
s:str = "Mississipi"
print(sorted([(item,s.count(item)) for item in set(s)]))

date1 = "Apr 30 2020"
d1 = datetime.strptime(date1, "%b %d %Y")
d2 = d1 - timedelta(weeks=1)
print(datetime.strftime(d2,"%b %d %Y"))

