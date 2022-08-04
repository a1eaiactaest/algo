import numpy as np
from typing import List, Union, Tuple

import vectors

MVal = Union[int, float]
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
  def __init__(self, rows: List[List[MVal]]) -> None:
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

  def cols(self, i: int) -> List[MVal]:
    """Return columns in array, rotate by 90* left."""
    ret = []
    for row in self.rows:
      ret.append(row[i])
    return ret

  def identity(self) -> "Matrix":
    ret = [
      [0 if column_n != row_n else 1 for column_n in range(self.m)]
      for row_n in range(self.n)
    ]
    return Matrix(ret)

  # **** Comparison Operators ****
  def __eq__(self, other) -> bool:
    return self.rows == other.rows

  def __ne__(self, other) -> bool:
    return not (self.rows == other.rows)

  def __gt__(self, other) -> bool:
    return (self.shape > other.shape)

  # **** Arithmetic Operators ****
  def __mul__(self, other) -> "Matrix":
    if type(other) is int:
      return self.rows * other
    elif type(other) is Matrix:
      if self.n != other.m:
        raise ArithmeticError(
          f"can't multiply matrix of shape {self.shape} by other matrix of shape {other.shape}."
        )
      ret_matrix = zeros((self.m, other.n))
      for row, i in zip(self.rows, range(self.m)): 
        for j in range(other.n):
          col = other.cols(j)
          product = vectors.dot(row, col) 
          ret_matrix[i][j] = product
      
    return Matrix(ret_matrix)

  def __repr__(self) -> str:
    pstr = ('\n'+' '*7).join([str(row) for row in self.rows])
    return f"Matrix({pstr})"


def zeros(shape: Tuple[int]) -> List[List[int]]:
  rows, cols = shape
  ret = [[0 for _ in range(cols)] for _ in range(rows)]
  return ret

if __name__ == "__main__":
  m1 = [[1,2,3],[4,5,6],[7,8,9], [10,11,12]]
  m2 = [[1,2,3],[4,5,6],[7,8,9], [10,11,12], [13,14,15]]
  M1 = Matrix(m1)
  M2 = Matrix(m2)
  print(M1 == M2)
  print(M1 != M2)
  print(M1 > M2)
  A = Matrix(np.array([[1,4,-2], [3,5,-6]]))
  B = Matrix(np.array([[5,2,8], [3,6,4]]))
  A = Matrix([[2,2],[2,2]])
  B = Matrix([[2,2],[2,2]])
  AB = Matrix([[4,4],[4,4]])
  print(A*B)
  print(AB.identity())