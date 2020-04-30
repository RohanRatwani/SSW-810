from typing import List

'''Here we'll see ways to return a copy list'''
def list_copy(lst:List):

    lst1 = lst.copy()
    lst2 = lst[:]
    lst.append(10)
    print(lst)
    return lst1, lst2

def list_max(lst:List):
    '''Here we'll see ways to return a max value of list'''
    max_val = max(lst)
    return "Max value in List is: ",max_val

def flatten_3a(l1:List):
    '''Here we'll see ways to flatten a list'''
    l2 : List = []
    l3 : List = []
    '''3a'''
    for item in l1:
        for i in item:
            l2.append(i)
    return l2

def flatten_3b(l1: List):
    '''3b'''
    return [i for item in l1 for i in item]

if __name__ == '__main__':
    print(list_copy(['1', '2', '3', '4', '5']))
    print(list_max(['1', '2', '3', '4', '5']))
    print(flatten_3a([[1,2],[3,4,5]]))
    print(flatten_3b([[1, 2], [3, 4, 5]]))
