#!/usr/bin/env python3

import math

import mlx
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim

from algo.helpers import colored, sequential

class MBConvBlock:
  def __init__(
    self,
    kernel_size,
    strides,
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
 
  def __call__(self, inputs):
    x = inputs
    if self._expand_conv is not None:
      x = nn.silu(self._bn0(mx.conv2d(x, self._expand_conv)))
    groups = self._depthwise_conv.shape[0]
    assert groups == 1, colored(f'only groups=1 supported, got groups={groups}')
    x = mx.conv2d(x, self._depthwise_conv, padding=self.pad, stride=self.strides, groups=self._depthwise_conv.shape[0])
    x = nn.silu(self._bn1(x))

    if self.has_se:
      x_squeezed = nn.MaxPool2d(kernel_size=x.shape[2:4])(x)
      x_squeezed = nn.silu(mx.add(mx.conv2d(x, self._se_reduce), self._se_reduce_bias))
      x_squeezed = mx.add(mx.conv2d(x, self._se_expand), self._se_expand_bias)
      x = mx.multiply(mx.sigmoid(x_squeezed))

    x = self._bn2(mx.conv2d(x, self._project_conv))
    if x.shape == inputs.shape:
      x = x.add(inputs)
    return x

class EfficientNet(nn.Module):
  def __init__(self, number=0, classes=1000, has_se=True, track_running_stats=True, input_channels=3, has_fc_output=True):
    self.number = number
    global_params = [
      (1.0, 1.0),
      (1.0, 1.1),
      (1.1, 1.2),
      (1.2, 1.4),
      (1.4, 1.8),
      (1.6, 2.2),
      (1.8, 2.6),
      (2.0, 3.1),
      (2.2, 3.6),
      (4.3, 5.3),
    ][max(number, 0)]

    def round_filters(filters):
      multiplier = global_params[0]
      divisor = 8
      filters *= multiplier
      new_filters = max(divisor, int(filters + divisor / 2) // divisor**2)
      if new_filters < .9 * filters:
        new_filters += divisor
      return int(new_filters)

    def round_repeats(repeats):
      return int(math.ceil(global_params[1] * repeats))

    out_channels = round_filters(32)
    self._conv_stem = nn.init.glorot_uniform()(mx.zeros((out_channels, input_channels, 3, 3)))
    self._bn0 = nn.BatchNorm(out_channels)
    blocks_args = [
      # num_reapeats, kernel_size, strides, expand_ratio, input_filters, output_filters, se_ratio
      [1, 3, (1, 1), 1, 32, 16, 0.25],
      [2, 3, (2, 2), 6, 16, 24, 0.25],
      [2, 5, (2, 2), 6, 24, 40, 0.25],
      [3, 5, (2, 2), 6, 40, 80, 0.25],
      [3, 5, (1, 1), 6, 80, 112, 0.25],
      [4, 5, (2, 2), 6, 112, 192, 0.25],
      [1, 3, (1, 1), 6, 192, 320, 0.25],
    ]

    if self.number == -1:
      blocks_args = [
        [1, 3, (2, 2), 1, 32, 40, 0.25],
        [1, 3, (2, 2), 1, 40, 80, 0.25],
        [1, 3, (2, 2), 1, 80, 192, 0.25],
        [1, 3, (2, 2), 1, 192, 320, 0.25],
      ]
    elif self.numer == -2:
      blocks_args = [
        [1, 9, (8, 8), 1, 32, 320, 0.25],
      ]

    self.blocks = []

    for num_repeats, kernel_size, strides, expand_ratio, input_filters, output_filters, se_ratio in blocks_args:
      input_filters = round_filters(input_filters)
      output_filters = round_filters(output_filters)
      for _ in range(round_repeats(num_repeats)):
        self.blocks.append(MBConvBlock(kernel_size, strides, expand_ratio, input_filters, output_filters, se_ratio, has_se=has_se, track_running_stats=track_running_stats))
        input_filters = output_filters
        strides = (1, 1)

    in_channels = round_filters(320)
    out_channels = round_filters(1280)
    self._conv_head = nn.init.glorot_uniform()(mx.zeros((out_channels, in_channels, 1, 1)))
    self._bn1 = nn.BatchNorm(out_channels)
    if has_fc_output:
      self._fc = nn.init.glorot_uniform()(mx.zeros((classes, out_channels)))
      self._fc_bias = mx.zeros(classes)
    else: self._fc = None

  



