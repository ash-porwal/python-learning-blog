"""
- What are sequence type objects ?
    Sequence will be any object which
    - items are ordered
    - we can iterate each item: means that object has __iter__ function
    - we can access each item with integer index: means it has __getitem__() function
    - we can count the length: means it has __len__() function

- example of sequence type: string, list, tuples, range()
"""
# wait a minute range is sequence?
# so here is example:
# >>> numbers = range(5, 11)
# >>> len(numbers) # we can count lenght
# 6
# >>> numbers[1] # we can get item via interger index
# 6
# >>> numbers[1:5] # we can slice it
# range(6, 10) # and obviously we can iterate it
# >>> 

"""
- as sequence support getitem method, so we can slice it as well.

    But it is possible that sequences may not support slicing.
    Example: deque data type from collection
    
- Concatenating Sequences
    Two same sequence type can be concatenated easily but
    can't add sequences of different types

    Example:

    - Same type
        >>> [1, 2, 3] + [4, 5, 6]
            [1, 2, 3, 4, 5, 6]

        >>> (1, 2, 3) + (4, 5, 6)
            (1, 2, 3, 4, 5, 6)

    - different type:
        >>> range(10) + range(10, 20, 2)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'range' and 'range'


    -  example of a sequence that can't be concatenated even in case of same type:
        >>> range(10) + range(10, 20, 2)
        Traceback (most recent call last):
        ...
        TypeError: unsupported operand type(s) for +: 'range' and 'range'
"""

# Using Abstract Base Class
"""
- The abstract base class collections.abc.Sequence provides a template that defines 
  the interface for most sequences.
  We can find out whether a data type is a sequence or not

    >>> from collections.abc import Sequence
    >>> isinstance([2, 4, 6], Sequence)
    True
    >>> isinstance((2, 4, 6), Sequence)
    True
    >>> isinstance({2, 4, 6}, Sequence)
    False
    >>> isinstance({"A Key": "A Value"}, Sequence)
    False
"""

# When an object can be mutable and immutable?
"""
- When in object we have function
    .__setitem__()
    .__delitem__()
    .insert()
  then that object is mutable. If that objet does not have those function
  then it is immutable.
"""

# My custom class which behaves like a sequence
class MySeq:
    def __init__(self, elements):
        self.elements = list(elements)

    def __len__(self):
        return len(self.elements)

    def __getitem__(self, index):
        return self.elements[index]

numbers = MySeq([1, 2, 3, 4, 5])