import re

def ints(string):
  """Takes a string and returns all ints in it.
  
  _Example:

    >>> ints(string)
    [2, 1]
    >>> ints("my favorite number is 1337, not one thousand three hundred thirty seven")
    [1337]
    >>> ints("he33llo 42 I'm a 32 string 30")
    [33, 42, 30]

  """

  return [int(s) for s in re.findall(r'\b\d+\b', string)]