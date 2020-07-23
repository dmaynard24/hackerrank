from functools import cmp_to_key


class Player:
  def __init__(self, name, score):
    self.name = name
    self.score = score


def comparator(a, b):
  if a.score > b.score:
    return -1
  elif a.score < b.score:
    return 1
  else:
    if a.name > b.name:
      return 1
    else:
      return -1


def sorting_comparator(arr):
  players = []
  for s in arr:
    name, score = s.split()
    players.append(Player(name, int(score)))

  players = sorted(players, key=cmp_to_key(comparator))
  return '\n'.join([f'{p.name} {p.score}' for p in players])