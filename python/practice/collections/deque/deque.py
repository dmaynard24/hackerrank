from collections import deque as dq


def deque(operations):
  d = dq()
  for operation in operations:
    i = operation.split()
    if i[0] == 'append':
      d.append(i[1])
    elif i[0] == 'appendleft':
      d.appendleft(i[1])
    elif i[0] == 'pop':
      d.pop()
    elif i[0] == 'popleft':
      d.popleft()
  return ' '.join(d)
