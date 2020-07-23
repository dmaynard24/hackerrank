def is_strict_superset(sup, subs):
  sup = set(sup)

  is_ss = True
  for sub in subs:
    sub = set(sub)
    is_ss = is_ss and len(sup.difference(sub)) > 0 and len(
        sub.difference(sup)) == 0

  return is_ss