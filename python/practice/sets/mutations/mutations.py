def mutations(s, cmds):
  s = set(s)

  for cmd in cmds:
    c = cmd[0].split()
    new_s = set(cmd[1])
    if c[0] == 'intersection_update':
      s.intersection_update(new_s)
    elif c[0] == 'update':
      s.update(new_s)
    elif c[0] == 'symmetric_difference_update':
      s.symmetric_difference_update(new_s)
    elif c[0] == 'difference_update':
      s.difference_update(new_s)

  return sum(map(int, s))