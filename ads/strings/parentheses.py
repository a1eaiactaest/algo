def valid(line: str) ->  bool:
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