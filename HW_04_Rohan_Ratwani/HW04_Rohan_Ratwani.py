from typing import Any, List, Optional, Sequence, Iterator

def count_vowels(s : str) -> int:
    ''' return the number of vowels in the strings '''
    count: int = 0
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u']:
            count += 1
    #print(count)
    return count

def last_occurence(target: Any, seq: Sequence[Any]) -> Optional[int]:
    ''' return the offset from 0 of the last occurrence of target in seq '''
    i:int=0
    j:List=[]
    while i<len(seq):
        if target in seq:
            j.append(i)
        i=i+1
    if len(j)!= 0:
        return j[-1]
    else:
        return  None



def my_enumerate(seq: Sequence[Any]) -> Iterator[Any]:
    """ emulate the behavior of Python's built in enumerate() function.
        For each call, return a tuple with the offset from 0 and the next item
    """
    def mini(seq):
        for i in range(len(seq)):
            yield i,seq[i]  # replace with implementation

    list1:List=[]
    for i in mini(seq):
        list1.append(i)
    return list1

