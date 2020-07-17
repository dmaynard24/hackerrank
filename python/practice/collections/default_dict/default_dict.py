from collections import defaultdict


def default_dict(a_words, b_words):
  a = defaultdict(list)
  for i, word in enumerate(a_words):
    a[word].append(str(i + 1))
  return '\n'.join([' '.join(a.get(word, ['-1'])) for word in b_words])
