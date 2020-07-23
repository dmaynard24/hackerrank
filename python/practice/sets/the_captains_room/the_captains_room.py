def the_captains_room(k, l):
  s = set(l)
  return ((sum(s) * k) - sum(l)) // (k - 1)