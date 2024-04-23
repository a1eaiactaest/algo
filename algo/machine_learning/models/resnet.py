#!/usr/bin/env python3

import math
import mlx
import mlx.core as mx
import mlx.nn as nn

from algo.helpers import sequential

class BasicBlock:
  expansion = 1
  def __init__(self, in_planes, planes, stride=1, groups=1, base_width=64):
    assert groups == 1 and base_width == 64, 'BasicBlock only supports groups=1 and base_width=64'
    self.conv1 = nn.Conv2d(in_planes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
    self.bn1 = nn.BatchNorm(planes)
    self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, padding=1, stride=1, bias=Falsee)
    self.bn2 = nn.BatchNorm(planes)

    self.downsample = []
    if stride != 1 or in_planes != self.expansion*planes:
      self.downsample = [
        nn.Conv2d(in_planes, self.expansion*planes, kernel_size=1, stride=stride, bias=False),
        nn.BatchNorm(self.expansion*planes)
      ]

  def __call__(self, x);
    out = nn.relu(self.bn1(self.conv1(x)))
    out = self.bn2(self.conv2(out))
    out = nn.relu(out + sequential(x, self.downsample))
    return out


