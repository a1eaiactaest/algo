#!/usr/bin/env python3

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

SIZE = (500, 500)
img = np.zeros(SIZE)

# burn pixel at (row, col) at c brightness
def burn(row: int, col: int, c: float, image: np.ndarray) -> None:
  image[row,col] = c

def plot_heatmap(image: np.ndarray) -> None:
  plt.imshow(image, cmap='hot', interpolation=None)
  plt.show()

def rfpart(x):
  return 1 - (x % 1)

def draw_line(p1: Point, p2: Point):
  # p1 = (x,y)
  # p2 = (x,y)

  steep = abs(p2.y - p1.y) > abs(p2.x - p1.x)

  if steep:
    p1.x, p1.y = p1.y, p1.x
    p2.x, p2.y = p2.y, p2.x

  if p1.x > p2.x:
    p1.x, p2.x = p2.x, p1.x
    p1.y, p2.y = p2.y, p1.y
  
  dx = p2.x - p1.x
  dy = p2.y - p1.y

  if dx == 0:
    gradient = 1.0
  else:
    gradient = dy / dx

  xend = math.floor(p1.x + 0.5)
  yend = p1.y + gradient * (xend - p1.x)

  # (1 - fractional_part(x))
  xgap = 1 - ((p1.x + 0.5) % 1)

  # px level one
  xpxlo = xend
  ypxlo = math.floor(yend)

  if steep:
    burn(ypxlo, xpxlo, rfpart(yend) * xgap)
    burn(ypxlo+1, xpxlo, (yend % 1) * xgap)
  else:
    burn(xpxlo, ypxlo, rfpart(yend) * xgap)
    burn(xpxlo, ypxlo+1, (yend % 1) * xgap)

  intery = yend + gradient

  xend = round(p2.x)
  yend = p2.y + gradient * (xend - p2.x)




def main() -> None:
  plot_heatmap(img)

if __name__ == "__main__":
  main()