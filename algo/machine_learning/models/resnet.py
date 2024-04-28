#!/usr/bin/env python3

import math
import mlx
import mlx.core as mx
import mlx.nn as nn

from algo.helpers import sequential, torch_load, fetch, get_child

class BasicBlock(nn.Module):
  expansion = 1
  def __init__(self, in_planes, planes, stride=1, groups=1, base_width=64):
    super().__init__()
    assert groups == 1 and base_width == 64, 'BasicBlock only supports groups=1 and base_width=64'
    self.conv1 = nn.Conv2d(in_planes, planes, kernel_size=3, stride=stride, padding=1, bias=False)
    self.bn1 = nn.BatchNorm(planes)
    self.conv2 = nn.Conv2d(planes, planes, kernel_size=3, padding=1, stride=1, bias=False)
    self.bn2 = nn.BatchNorm(planes)

    self.downsample = []
    if stride != 1 or in_planes != self.expansion*planes:
      self.downsample = [
        nn.Conv2d(in_planes, self.expansion*planes, kernel_size=1, stride=stride, bias=False),
        nn.BatchNorm(self.expansion*planes)
      ]

  def __call__(self, x):
    out = nn.relu(self.bn1(self.conv1(x)))
    out = self.bn2(self.conv2(out))
    out = nn.relu(out + sequential(x, self.downsample))
    return out

class Bottleneck(nn.Module):
  expansion = 4
  def __init__(self, in_planes, planes, stride=1, groups=1, base_width=64):
    super().__init__()
    width = int(planes * (base_width / 64.0)) * groups

    self.conv1 = nn.Conv2d(in_planes, width, kernel_size=1, stride=1, bias=False)
    self.bn1 = nn.BatchNorm(width)
    self.conv2 = nn.Conv2d(width, width, kernel_size=3, padding=1, groups=groups, stride=1, bias=False)
    self.bn2 = nn.BatchNorm(width)    
    self.conv3 = nn.Conv2d(width, self.expansion*planes, kernel_size=1, bias=False)
    self.bn3 = nn.BatchNorm(self.expansion*planes)
    self.downsample = []
    if stride != 1 or in_planes != self.expansion*planes:
      self.downsample = [
        nn.Conv2d(in_planes, self.expansion*planes, kernel_size=1, stride=stride, bias=False),
        nn.BatchNorm(self.expansion*planes)
      ]

  def __call__(self, x):
    out = nn.relu(self.bn1(self.conv1(x)))
    out = nn.relu(self.bn2(self.conv2(x)))
    out = self.bn3(self.conv3(out))
    out = nn.relu(out + sequential(x, self.downsample))
    return out


class ResNet(nn.Module):
  def __init__(self, num, num_classes=None, groups=1, width_per_group=64, stride_in_1x1=False):
    self.num = num
    self.block = {
      18: BasicBlock,
      34: BasicBlock,
      50: Bottleneck,
      101: Bottleneck,
      152: Bottleneck
    }[num]

    self.num_blocks = {
      18: [2,2,2,2],
      34: [3,4,6,3],
      50: [3,4,6,3],
      101:[3,4,23,3],
      152:[3,8,36,3],
    }[num]

    self.in_planes = 64
    self.groups = groups
    self.base_width = width_per_group

    self.conv1 = nn.Conv2d(3, 64, kernel_size=7, stride=2, padding=3, bias=False)
    self.bn1 = nn.BatchNorm(64)
    self.layer1 = self._make_layer(self.block, 64, self.num_blocks[0], stride=1)
    self.layer2 = self._make_layer(self.block, 128, self.num_blocks[1], stride=2)
    self.layer3 = self._make_layer(self.block, 256, self.num_blocks[2], stride=2)
    self.layer4 = self._make_layer(self.block, 512, self.num_blocks[3], stride=2)
    self.fc = nn.Linear(512 * self.block.expansion, num_classes) if num_classes is not None else None

  def _make_layer(self, block, planes, num_blocks, stride):
    strides = [stride] + [1] * (num_blocks - 1)
    layers = []
    for stride in strides:
      layers.append(block(self.in_planes, planes, stride, self.groups, self.base_width))
      self.in_planes = planes * block.expansion
    return layers
  
  def __call__(self, x):
    is_feature_only = self.fc is None
    if is_feature_only: 
      features = []
    out = nn.relu(self.bn1(self.conv1(x)))
    out = nn.MaxPool2d((3,3), 2)(mx.pad(out, 1))
    out = sequential(out, self.layer1)
    if is_feature_only: features.append(out)
    out = sequential(out, self.layer2) 
    if is_feature_only: features.append(out)
    out = sequential(out, self.layer3) 
    if is_feature_only: features.append(out)
    out = sequential(out, self.layer4) 
    if is_feature_only: features.append(out)
    if not is_feature_only:
      out = mx.mean(out, (2,3))
      out = self.fc(out.astype('float32'))
      return out
    return features

  def load_pretrained(self):
    urls = {
      (18, 1 ,64): 'https://download.pytorch.org/models/resnet18-5c106cde.pth',
      (34, 1 ,64): 'https://download.pytorch.org/models/resnet34-333f7ec4.pth',
      (50, 1 ,64): 'https://download.pytorch.org/models/resnet50-19c8e357.pth',
      (50, 32, 4): 'https://download.pytorch.org/models/resnext50_32x4d-7cdf4587.pth',
      (101, 1 ,64): 'https://download.pytorch.org/models/resnet101-5d3b4d8f.pth',
      (152, 1 ,64): 'https://download.pytorch.org/models/resnet152-b121ed2d.pth',
    }

    self.url = urls[(self.num, self.groups, self.base_width)]
    for k, v in torch_load(fetch(self.url)).items():
      obj = get_child(self, k)
      dat = mx.array(v)

      if 'fc.' in k and obj.shape != dat.shape:
        print('skipping fully connected layer')
        continue

      assert obj.shape == dat.shape or (obj.shape == (1,) and dat.shape == ()), (k, obj.shape, dat.shape) 

_num_classes = 1000
ResNet18 = ResNet(18, num_classes=_num_classes)
ResNet34 = ResNet(34, num_classes=_num_classes)
ResNet50 = ResNet(50, num_classes=_num_classes)
ResNet101 = ResNet(101, num_classes=_num_classes)
ResNet152 = ResNet(152, num_classes=_num_classes)
ResNetXt50_32x4D = ResNet(50, num_classes=_num_classes, groups=32, width_per_group=4)
