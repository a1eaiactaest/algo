from typing import List, Union
def least_squares(X: List[Union[int,float]], Y:List[Union[int,float]]):
  assert len(X) == len(Y)

  N = len(X)

  X_mean = sum(X)/len(X)
  Y_mean = sum(Y)/len(Y)
  
  X_sigma = sum(X)
  Y_sigma = sum(Y)

  XY_sigma = 0
  X_squared_sigma = 0

  for x,y in zip(X,Y):
    XY_sigma += x*y
    X_squared_sigma += x**2
    
  slope = ((N * XY_sigma) - (X_sigma * Y_sigma)) / ((N * X_squared_sigma) - (X_sigma)**2)
  y_intercept = (Y_sigma - slope * X_sigma) / N

  slope_intercept = lambda x: (slope * x) + y_intercept

  estimates = []
  for x,y in zip(X,Y):
    estimation_y = slope_intercept(x)
    estimates.append(estimation_y)

  return estimates, slope, y_intercept