max_depth = 0


def find_max_depth(root):
  def depth(elem, level):
    children = list(elem)
    if len(children) == 0:
      global max_depth
      max_depth = max(max_depth, level + 1)
    else:
      for el in children:
        depth(el, level + 1)

  depth(root, -1)
  return max_depth