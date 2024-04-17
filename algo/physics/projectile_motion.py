from math import sin, radians

# Read: https://en.wikipedia.org/wiki/Projectile_motion

G = 9.81

def valid_args(v0: float, angle: float) -> None:
  if not isinstance(v0, (float, int)):
    raise TypeError("v0 must be a float or int")

  if not isinstance(angle, (float, int)):
    raise TypeError("angle must be a float or int")

  if not 1 <= angle <= 90:
    raise ValueError("angle has to be in between 1 and 90")

  if v0 < 0:
    raise ValueError("v0 can't be a nagative number")


def distance(v0: float, angle: float) -> float:
  """Return distance traveled by an object.
  All values are in SI units.
  Formula:

  d = (v0**2 * sin(2 * angle)) / g

  """
  valid_args(v0, angle)
  return round((v0**2/G)*sin(2 * radians(angle)), 3)

def max_height(v0: float, angle: float) -> float:
  """Return maximum height of projectile.
  Formula:

  h_max = ((v0**2) * sin(angle)**2)) / 2g

  """
  valid_args(v0, angle)
  return round(((v0**2) * sin(radians(angle))**2) / (2 * G), 3)

def time_to_max_height(v0: float, angle: float) -> float:
  """Return time to reach maximum height of projectile trajectory.
  Formula:
  th = (v0 * sin(angle)) / g
  """
  valid_args(v0, angle)
  return round((v0 * sin(radians(angle))) / G, 3)

def total_time(v0: float, angle: float) -> float:
  """Return total time of flight.
  Formula:
  t = (2v0 * sin(angle)/g)
  """
  valid_args(v0, angle)
  return round((2 * v0 * sin(radians(angle))) / G, 3)

if __name__ == "__main__":
  v0 = 55.5
  angle = 30
  print(distance(v0, angle))
  print(max_height(v0, angle))
  print(time_to_max_height(v0, angle))
  print(total_time(v0, angle))