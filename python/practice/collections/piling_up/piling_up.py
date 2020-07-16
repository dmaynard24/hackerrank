def is_valid_pile(pile):
  l = 0
  r = len(pile) - 1
  prev_val = None

  while l < r:
    if pile[l] >= pile[r]:
      if prev_val and pile[l] > prev_val:
        return False
      prev_val = pile[l]
      l += 1
    else:
      if prev_val and pile[r] > prev_val:
        return False
      prev_val = pile[r]
      r -= 1

  return True