def valid(line: str) ->  bool:
  stack = []
  p = {')':'(', '}': '{', ']':'['}

  for c in line:
    if c in p:
      if stack and stack[-1] == p[c]:
        stack.pop()
      else:
        return False
    else:
      stack.append(c)
  if not stack:
    return True
  return False
