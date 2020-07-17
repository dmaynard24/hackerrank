from collections import OrderedDict


def word_order(words):
  od = OrderedDict()
  for w in words:
    od[w] = od.get(w, 0) + 1
  print(len(od))
  print(*od.values())
