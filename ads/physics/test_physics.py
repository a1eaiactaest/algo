import unittest

import projectile_motion as pm

v0 = 55.5
angle = 30

class TestPhysics(unittest.TestCase):
  def test_distance(self):
    self.assertEqual(pm.distance(v0, angle), 271.924)

  def test_max_height(self):
    self.assertEqual(pm.max_height(v0, angle), 39.249)

  def test_time_to_m_height(self):
    self.assertEqual(pm.time_to_max_height(v0, angle), 2.829)

  def test_total_time(self):
    self.assertEqual(pm.total_time(v0, angle), 5.657)

class TestPhysicsExceptions(unittest.TestCase):
  def test_wrong_types(self):
    v0 = '1337'
    angle = True
    with self.assertRaises(TypeError):
      pm.distance(v0, angle)

  def test_angle_out_of_range(self):
    v0 = 10
    angle = 91
    with self.assertRaises(ValueError):
      pm.max_height(v0, angle)