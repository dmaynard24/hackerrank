def is_subset(sup, sub):
  sup, sub = set(sup), set(sub)
  return len(sup) == len(sup.intersection(sub))