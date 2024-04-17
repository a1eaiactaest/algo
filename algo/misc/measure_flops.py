#!/usr/bin/env python3

import time

import mlx.core as mx
import torch
import numpy as np
import tensorflow as tf

from algo.math.matrix import Matrix
from algo.helpers import Timing, MeasureFLOPS


N = 2048
flop = 2*(N**3)

def GeMM_numpy():
  A = np.random.randn(N, N).astype(np.float32)
  B = np.random.randn(N, N).astype(np.float32)
  with MeasureFLOPS(flop, unit_prefix='G', prefix='np'):
    C = A @ B

def GeMM_torch():
  A = torch.randn((N,N), dtype=torch.float32)
  B = torch.randn((N,N), dtype=torch.float32)

  with MeasureFLOPS(flop, unit_prefix='G', prefix='torch'):
    C = A @ B

def GeMM_tensorflow():
  A = tf.random.normal((N,N)) # dtype already as float32
  B = tf.random.normal((N,N)) 

  with MeasureFLOPS(flop, unit_prefix='G', prefix='tf'):
    C = A @ B

def GeMM_mlx():
  A = mx.random.normal([N,N]) # default dtype also is f32 
  B = mx.random.normal([N,N]) 
 
  with MeasureFLOPS(flop, unit_prefix='T', prefix='mlx'):
    C = A @ B

# too slow
'''
def GeMM_ads():
  A = Matrix(np.random.randn(N,N).tolist())
  B = Matrix(np.random.randn(N,N).tolist())
  
  with MeasureFLOPS(flop, unit_prefix='G', prefix='ads'):
    C = A @ B
'''

if __name__ == '__main__':
  GeMM_numpy() 
  GeMM_torch()
  GeMM_tensorflow()
  GeMM_mlx()
  #GeMM_ads()
