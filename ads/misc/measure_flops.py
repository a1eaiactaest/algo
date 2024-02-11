#!/usr/bin/env python3

import time

import mlx.core as mx
import torch
import numpy as np
import tensorflow as tf

from ads.math.matrix import Matrix
from ads.helpers import Timing, MeasureFLOPS


N = 2048
flop = 2*(N**3)

def GeMM_numpy():
  A = np.random.randn(N, N).astype(np.float32)
  B = np.random.randn(N, N).astype(np.float32)
  st = time.monotonic()   
  C = A @ B
  et = time.monotonic()
  s = et-st
  flops = flop/s
  print(f'np: {(flops * 1e-9):.2f} GFLOPS, {(s*1e3):.2f} ms')

def GeMM_torch():
  A = torch.randn((N,N), dtype=torch.float32)
  B = torch.randn((N,N), dtype=torch.float32)

  st = time.monotonic()
  C = A @ B
  et = time.monotonic()
  s = et-st
  flops = flop/s
  print(f'torch: {(flops * 1e-9):.2f} GFLOPS, {(s*1e3):.2f} ms')

def GeMM_tensorflow():
  A = tf.random.normal((N,N)) # dtype already as float32
  B = tf.random.normal((N,N)) 

  st = time.monotonic()
  C = A @ B
  et = time.monotonic()
  s = et-st
  flops = flop/s
  print(f'tf: {(flops * 1e-9):.2f} GFLOPS, {(s*1e3):.2f} ms')

def GeMM_mlx():
  A = mx.random.normal([N,N]) # default dtype also is f32 
  B = mx.random.normal([N,N]) 
 
  with MeasureFLOPS(flop, unit_prefix='T'):
    C = A @ B
  '''
  et = time.monotonic()
  s = et-st
  flops = flop/s
  print(f'mlx: {(flops * 1e-9):.2f} GFLOPS, {(s*1e3):.2f} ms')
  '''


if __name__ == '__main__':
  GeMM_numpy() 
  GeMM_torch()
  GeMM_tensorflow()
  GeMM_mlx()
