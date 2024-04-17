def quicksort(arr: list) -> list:
  if len(arr) < 2:
    return arr
  else:
    piv = arr[0]
    lower = [x for x in arr[1:] if x <= piv]
    upper = [x for x in arr[1:] if x > piv]
    return quicksort(lower) + [piv] + quicksort(upper)