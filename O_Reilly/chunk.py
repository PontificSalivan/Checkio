from typing import Iterable
import math

def chunking_by(items: list, size: int) -> Iterable:

    return [items[size*i:size*(i+1)] for i in range(math.ceil(len(items)/size))]

if __name__ == '__main__':
    print("Example:")
    print(list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(chunking_by([5, 4, 7, 3, 4, 5, 4], 3)) == [[5, 4, 7], [3, 4, 5], [4]]
    assert list(chunking_by([3, 4, 5], 1)) == [[3], [4], [5]]
    assert list(chunking_by([5, 4], 7)) == [[5, 4]]
    assert list(chunking_by([], 3)) == []
    assert list(chunking_by([4, 4, 4, 4], 4)) == [[4, 4, 4, 4]]
    print("Coding complete? Click 'Check' to earn cool rewards!")
