from collections import OrderedDict


def ordered_dict(items):
  od = OrderedDict()
  for i in items:
    ri = i.rindex(' ')
    k, v = i[:ri], i[ri:]
    od[k] = od.get(k, 0) + int(v)
  return '\n'.join([f'{k} {od[k]}' for k in od])
