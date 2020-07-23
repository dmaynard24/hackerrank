def check_magazine(magazine, note):
  mag_word_counts = {}
  for word in magazine:
    if word in mag_word_counts:
      mag_word_counts[word] += 1
    else:
      mag_word_counts[word] = 1

  for word in note:
    if word in magazine:
      mag_word_counts[word] -= 1
      if mag_word_counts[word] < 0:
        return 'No'
    else:
      return 'No'

  return 'Yes'
