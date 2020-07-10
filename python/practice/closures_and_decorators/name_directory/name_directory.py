def person_lister(f):
  def inner(people):
    return [f(p) for p in sorted(people, key=lambda p: int(p[2]))]

  return inner


@person_lister
def name_format(person):
  return ('Mr. ' if person[3] == 'M' else 'Ms. ') + person[0] + ' ' + person[1]


def name_directory(people):
  return '\n'.join(name_format(people))