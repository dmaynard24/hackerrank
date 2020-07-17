from collections import Counter


def company_logo(s):
  mc = sorted(Counter(sorted(s)).most_common(3),
              key=lambda c: c[1],
              reverse=True)
  return '\n'.join([' '.join(map(str, c)) for c in mc])
