from collections import Counter

def valid(w1: str, w2: str) -> bool:
  return Counter(w1) == Counter(w2)
