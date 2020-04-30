import random
from typing import Iterator,Optional,List

def random_integer_generator(minimum: int, maximum: int) -> Iterator[int]:
    #while True:
    #for i in range(0,10):#random.randint(minimum,maximum+1):
    i = random.randint(minimum,maximum)
    yield i  # return a random integer between 0 and 10 inclusive.

def find_target(target, min_value, max_value, max_attempts) -> Optional[int]:
    i:int = 0
    l:List =[]
    for _ in range(max_attempts):
        for i in random_integer_generator(min_value, max_value):
            print(i)
            print(target,"XYZ")
            if i == target:
                l.append(i)
                break
    return len(l),"ABC"

            # else:
            #     print(None)

print(find_target(3, 0, 3, 1))
