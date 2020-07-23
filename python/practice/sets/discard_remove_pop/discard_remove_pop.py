def discard_remove_pop(arr, cmds):
  s = set(arr)

  for cmd in cmds:
    cmd = cmd.split()
    if cmd[0] == 'pop':
      s.pop()
    elif cmd[0] == 'remove':
      s.remove(int(cmd[1]))
    elif cmd[0] == 'discard':
      s.discard(int(cmd[1]))

  return sum(s)
