import re


def get_substring_counts(sentences, words):
  counts = []
  for w in words:
    counts.append(
        sum([len(re.findall(r'(?<=\w)%s(?=\w)' % (w), s)) for s in sentences]))
  return '\n'.join(map(str, counts))