from collections import namedtuple


def named_tuple(col_names, grade_lines):
  Grade = namedtuple('Grade', *[col_names])
  grades = [Grade(*gl.split()) for gl in grade_lines]
  return sum([int(g.MARKS) for g in grades]) / len(grade_lines)
