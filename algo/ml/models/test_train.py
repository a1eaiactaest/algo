#!/usr/bin/env python3 

import unittest
import numpy as np
import time

import mlx
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim
from mlx.utils import tree_map, tree_flatten

from algo.helpers import getenv, colored, flatten_dict
from train import train
from resnet import ResNet18

BS = getenv('BS', 2)

def train_one_step(model: nn.Module, X, Y):
  params = model.parameters()
  pcount = sum(np.prod(v.shape) for _, v in tree_flatten(params))
  optimizer = optim.SGD(learning_rate=0.001)
  print("stepping %r with %.1fM params batch size %d" % (type(model), pcount/1e6, BS))
  st = time.time()
  train(model, X, Y, optimizer, 1, BS=BS)
  et = time.time()
  print("done in %.2f s" % ((et-st)*1000))


class TestTrain(unittest.TestCase):
  X = mx.zeros((BS, 3, 224, 244))
  Y = mx.zeros((BS,))
  model = ResNet18
  model.load_pretrained()
  train_one_step(model, X, Y)

if __name__ == "__main__":
  unittest.main()