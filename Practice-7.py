from typing import List,DefaultDict
from collections import Counter,defaultdict

def list_unique(seq:List):
    """a function list_unique(seq) that takes a sequence as an argument and returns a copy of seq that includes only the unique elements from seq"""
    y: List = []
    for i in seq.copy():
        if i not in y:
            y.append(i)
    return y

def no_repeats(S):
    """e a function no_repeats(s) that takes a string, s, and returns a string that consists of all of the characters in s rearranged so no two consecutive characters are the same, or return None if the string can't be arranged without repeated characters."""
    nr = Counter(S).most_common()
    #while b > 0:
    # for i in range(len(s)):
    #     print(nr[i][0])
    #     a = int(nr[i][1])
    #     b = a-1
    #     print(b)
    # a = (l[:(len(l)//2)])
    # b = (l[(len(l)//2):])
    # print(a,b)
    # # for i in a:
    # #     for j in b:
    # #         lst.append(i)
    # #         lst.append(j)
    # # for item in lst:
    # #     for i in item:
    # #         for j in i:
    # #             lst1.append(j)
    # # print("".join(str(v) for v in lst1))
    #  = [i + j for i, j in zip(a, b)]
    # print("".join(str(v) for v in ))

    lst = [(n, c) for c, n in nr]
    lst.sort()
    res: List = []
    n, c = lst[0]
    for i in range(int(nr[0][1])):
        res.append([nr[0][0]])

    cnt = 0
    for n, c in lst[1:]:
        for i in range(n):
            res[cnt].append(c)
            cnt = (cnt + 1) % len(res)

    if len(res) > 1 and len(res[-2]) == 1:
        return None

    return "".join(
        map(lambda x: "".join(x), res)
    )



if __name__ == '__main__':
    print(list_unique([1, 2, 1, 3, 4, 2, 4, 5]))
    print(no_repeats("aabb"))


