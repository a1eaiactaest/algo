from typing import List

class LinearRegression:
  def __init__(self, slope: float, y_intercept: float) -> None:
    self.slope = slope
    self.y_intercept = y_intercept

  def __repr__(self) -> str:
    return f'LinearRegression(slope={self.slope}, y_intercept={self.y_intercept})'


def least_squares(X: List[int | float], Y:List[int | float]) -> "LinearRegression":
  '''Linear regression using the least squares method.

  Reference: https://en.wikipedia.org/wiki/Least_squares

  :param X: Data on X axis.
  :type X: List[int | float]
  :param Y: Data on Y axis.
  :type Y: List[int | float]
  :return: Computed slope of a line and it's y-intercept conveyed in LinearRegression class.
  :rtype: LinearRegression
  '''

  assert len(X) == len(Y)
  
  xy_sigma = 0
  x_square_sigma = 0

  for x, y in zip(X,Y):
    xy_sigma += x*y
    x_square_sigma += x**2

  slope = ((len(X) * xy_sigma) - (sum(X) * sum(Y))) / ((len(X) * x_square_sigma) - (sum(X))**2)
  y_intercept = (sum(Y) - slope * sum(X)) / len(X)

  return LinearRegression(slope, y_intercept)


def predict(linreg: "LinearRegression", data: List[int | float]) -> List[float]:
  '''Fit line given linear regression values.

  Take :data: as y axis values, return x axis values prediction given slope and y_intercept.

  :param linreg: Linear regression values like slope and y-intercept.
  :type linreg: LinearRegression
  :param data: y axis values 
  :type data: List[int | float]
  :return: x axis values
  :rtype: List[float]
  '''

  ret = []
  slope_intercept = lambda x: (linreg.slope * x) + linreg.y_intrecept
  
  for v in range(len(data)):
    ret.append(slope_intercept(v))

  return ret

