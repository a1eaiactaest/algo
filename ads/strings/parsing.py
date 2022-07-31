def valid_parentheses(line: str) ->  bool:
  stack = []
  for c in line:
    if c in ['(', '[', '{']:
      stack.append(c)
    else:
      if stack == []:
        return False
      if c in [')', ']', '}']:
        stack.pop()
  if stack == []:
    return True
  return False

def postfix(line: str) -> float:
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
