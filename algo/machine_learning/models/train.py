import os
import mlx
import mlx.core as mx
import mlx.nn as nn
import mlx.optimizers as optim
import numpy as np
from tqdm import trange

CI = os.getenv("CI", "") != ""

def train(
    model: nn.Module,
    X_train,
    Y_train,
    optimizer: optim.Optimizer,
    steps: int,
    BS=128,
    loss_fn=lambda out, y: nn.losses.cross_entropy(out, y),
    transform=lambda x:x,
    target_transform=lambda x:x,
    noloss=False
    ):
  loss_and_grad_fn = nn.value_and_grad(model, loss_fn)
  def train_step(x: mx.array, y: mx.array) -> tuple[mx.array, mx.array]:
    out: mx.array = model(x)
    loss, grads = loss_and_grad_fn(model, out, y)
    if noloss: del loss
    optimizer.update(model, grads)
    if noloss: return (None, None)
    cat = out.argmax(axis=-1)
    accuraccy = (cat == y).mean()
    mx.eval(model.parameters(), optimizer.state)
    return loss, accuraccy
    
  losses, accuraccies = [], []
  for i in (t := trange(steps, disable=CI)):
    samp = np.random.randint(0, X_train.shape[0], size=(BS,))
    x = mx.array(transform(X_train[samp]))
    y = mx.array(target_transform(Y_train[samp]))
    loss, accuraccy = train_step(x, y)
    if not noloss:
      loss, accuraccy = loss.item(), accuraccy.item()
      losses.append(loss)
      accuraccies.append(accuraccy)
      t.set_description("loss %.2f accuraccy %.2f" % (loss, accuraccy))
  return [losses, accuraccies]
