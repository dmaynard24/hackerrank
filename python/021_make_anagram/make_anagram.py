def makeAnagram(a, b):
  def checkSharedChars(longer, shorter):
    deletion_count = 0
    longer_chars = {}
    for longer_char in list(longer):
      longer_chars[longer_char] = longer_chars.get(longer_char, 0) + 1
    for shorter_char in list(shorter):
      if shorter_char in longer_chars:
        longer_chars[shorter_char] -= 1
        if longer_chars[shorter_char] < 0:
          deletion_count += 1
      else:
        deletion_count += 1
    for longer_char_count in longer_chars.values():
      if longer_char_count > 0:
        deletion_count += longer_char_count
    return deletion_count

  if len(a) > len(b):
    return checkSharedChars(a, b)
  else:
    return checkSharedChars(b, a)


print(makeAnagram('cde', 'abc'))  # 4
print(makeAnagram('fcrxzwscanmligyxyvym',
                  'jxwtrhvujlmrpdoqbisbwhmgpmeoke'))  # 30
