def exp(x: float , n: int) -> float:
  if n < 0:
    x = 1 / x
    n *= -1
  if n == 0: return 1

  y = 1
  while n > 1:
    if n % 2 == 0:
      x *= x
      n /= 2
    else:
      y *= x
      x *= x
      n = (n-1)/2
  return x * y

def exp_r(x: float, n: int) -> float:
  if n < 0:
    return exp_r(1/x, -n)
  elif n == 0:
    return 1
  elif n % 2 == 0:
    return exp_r(x*x, n/2)
  elif n % 2 != 0:
    return x * exp_r(x*x, (n-1)/2)

