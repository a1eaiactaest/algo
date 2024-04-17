#!/usr/bin/env python3

import mlx
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

class MBConvBlock:
  def __init__(
    self,
    kernel_sizestrides,
    expand_ratio,
    input_filters,
    output_filters,
    se_ratio,
    has_se,
    track_running_stats=True
  ):
  self.has_se = has_se
  oup = expand_ratio * input_filters
  if expand_ratio != 1:
    self._expand_conv = nn.init.glorot_uniform()(mx.zeros((oup, input_filters, 1, 1)))
    self._b0 = nn.BatchNorm(oup)
  else:
    self._expand_conv = None

  self.strides = strides
  if strides == (2, 2): self.pad = [(kernel_size-1)//2-1, (kernel_size)//2]*2
  else: self.pad = [(kernel_size-1)//2]*4

  self._depthwise_conv = nn.init.glorot_uniform()(mx.zeros((oup, input_filters, 1, 1)))
  self._bn1 = nn.BatchNorm(oup)

  if self.has_se:
    num_squeezed_channels = max(1, int(input_filters * se_ratio))
    self._se_reduce = nn.init.glorot_uniform()(mx.zeros((oup, input_filters, 1, 1)))
    self.se_reduce_bias = mx.zeros(num_squeezed_channels)
    self._se_expand = nn.init.glorot_uniform()(mx.zeros((oup, input_filters, 1, 1)))
    self.se_expand_bias = mx.zeros(num_squeezed_channels)

  self._project_conv = nn.init.glorot_uniform()(mx.zeros((output_filters, oup, 1, 1)))
  self._bn2 = nn.BatchNorm(output_filters)


