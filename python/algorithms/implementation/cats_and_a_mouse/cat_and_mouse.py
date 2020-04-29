def cat_and_mouse(x, y, z):
  a_dist = abs(x - z)
  b_dist = abs(y - z)
  if a_dist < b_dist:
    return 'Cat A'
  elif a_dist > b_dist:
    return 'Cat B'
  else:
    return 'Mouse C'