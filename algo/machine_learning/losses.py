import numpy as np

def mean_squared_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
  if len(y_true) != len(y_pred):
    raise ValueError("y_true and y_pred must have the same length")
  return np.mean((y_true - y_pred)**2)

def mean_absolute_error(y_true: np.ndarray, y_pred: np.ndarray) -> float:
  if len(y_true) != len(y_pred):
    raise ValueError("y_true and y_pred must have the same length")
  return np.mean(np.absolute(y_pred - y_true))