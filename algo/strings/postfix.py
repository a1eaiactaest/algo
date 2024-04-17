def eval(line: str) -> float:
  ops = ['*', '+', '-', '/']
  stack = []
  if ' ' in line:
    broken_line = line.split()
  else:
    broken_line = list(line)

  for c in broken_line:
    if c in ops:
      b = stack.pop()
      a = stack.pop()
      if c == '*':
        stack.append(a*b)
      elif c == '+':
        stack.append(a+b)
      elif c == '-':
        stack.append(a-b)
      elif c == '/':
        stack.append(a/b)
    else:
      stack.append(float(c))
  return stack.pop()