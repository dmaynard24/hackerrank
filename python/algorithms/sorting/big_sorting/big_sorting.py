from functools import cmp_to_key


def big_sorting(unsorted):
  def asc(a, b):
    if len(a) > len(b):
      return 1
    elif len(a) == len(b):
      if int(a) > int(b):
        return 1
      else:
        return -1
    else:
      return -1

  return sorted(unsorted, key=cmp_to_key(asc))
