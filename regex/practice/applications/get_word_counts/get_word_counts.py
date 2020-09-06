import re


def get_word_counts(sentences, words):
  counts = []
  for w in words:
    counts.append(sum([len(re.findall(r'\b%s\b' % (w), s))
                       for s in sentences]))
  return '\n'.join(map(str, counts))