import re

def ints(string: str):
  """Takes a string and returns all ints in it in the sorted order.
  
  _Example:

    >>> ints("i have 1 cat and 2 dogs")
    [1, 2]
    >>> ints("my favorite number is 1337, not one thousand three hundred thirty seven")
    [1337]
    >>> ints("he33llo 42 I'm a 32 string 30")
    [30, 32, 33, 42]

  """

  return sorted([int(s) for s in re.findall(r'\d+', string)])
