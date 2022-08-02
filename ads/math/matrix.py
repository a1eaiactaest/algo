import numpy as np
from typing import List, Union, Tuple

class Matrix:
  """Matrix class in python.

  :reference: https://en.wikipedia.org/wiki/Matrix_(mathematics)#
  
  :param rows: a nd-array, numpy is supported.
    :rows: this variable can be either:
            * row vector
              >>> rows = [[1,2,3]] # 1 * n
              >>> M = Matrix(rows)
            * column vector
              >>> rows = [[1],[2],[3]] n * 1
              >>> M = Matrix(rows)
            * square matrix
              >>> rows = [[1],[2],[3]] n * n
              >>> M = Matrix(rows)
            * rectangular matrix
              >>> rows = [[1,2,3,4],[5,6,7,8],[9,10,11,12]] n * m
              >>> M = Matrix(rows)

  :type rows: nd-array, list of lists, List[List[int | float]]
  """
  def __init__(self, rows: List[List[Union[int, float]]]) -> None:
    self.rows = rows
    self._check()

  def _check(self) -> None:
    """Matrix validation.

    Raises TypeError if:
      * All rows aren't the same length.
      * self.rows length is <= 1

    _Example:

      >>> m = [[1,2,3],[4,5,6],[7,8,9]]
      >>> np.array(m)
      array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
      >>> Matrix(m)

      >>> m = [[1,2,3],[4,5],[7,8,9]]
      >>> np.array(m)
      array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
      >>> Matrix(m)
      TypeError: All rows are not the same length.
    """

    height = len(self.rows)
    width = len(self.rows[0])
    if height <= 1:
      raise TypeError("Matrix can't be sized 1 or empty, pass a 2d array.")
    for row in self.rows:
      if len(row) != width:
        raise TypeError("All rows are not the same length.")

  @property
  def m(self) -> int:
    """Amount of rows"""
    return len(self.rows)

  @property
  def n(self) -> int:
    """Amount of columns"""
    return len(self.rows[0])

  @property
  def shape(self) -> Tuple[int]:
    return (self.m, self.n)

  # **** Comparison Operators ****
  def __eq__(self, other) -> bool:
    return np.array_equal(self, other)

  def __gt__(self, other) -> bool:
    return (self.shape > other.shape)

  # **** Arithmetic Operators ****
  def __mul__(self, other):
    if type(other) is int:
      return self.rows * other
    elif type(other) is Matrix:
      raise NotImplementedError

if __name__ == "__main__":
  m1 = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
  m2 = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12], [13,14,15]])
  M1 = Matrix(m1)
  M2 = Matrix(m2)
  print(M1 == M2)
  print(M1 > M2)
