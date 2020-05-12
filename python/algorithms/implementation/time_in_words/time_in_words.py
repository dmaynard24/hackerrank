def time_in_words(h, m):
  words = {
      1: 'one',
      2: 'two',
      3: 'three',
      4: 'four',
      5: 'five',
      6: 'six',
      7: 'seven',
      8: 'eight',
      9: 'nine',
      10: 'ten',
      11: 'eleven',
      12: 'twelve',
      13: 'thirteen',
      14: 'fourteen',
      16: 'sixteen',
      17: 'seventeen',
      18: 'eighteen',
      19: 'nineteen'
  }

  if m == 0:
    return words[h] + ' o\' clock'

  time_str = ''
  original_m = m
  if m <= 30:
    if m == 30:
      time_str += 'half '
      m -= 30
    if m == 15:
      time_str += 'quarter '
      m -= 15
    if m >= 20:
      time_str += 'twenty '
      m -= 20
    if m > 0:
      time_str += words[m] + ' minute'
      time_str += 's ' if original_m > 1 else ' '
    time_str += 'past ' + words[h]
  else:
    m = 60 - m
    if m == 15:
      time_str += 'quarter '
      m -= 15
    if m >= 20:
      time_str += 'twenty '
      m -= 20
    if m > 0:
      time_str += words[m] + ' minute'
      time_str += 's ' if original_m > 1 else ' '
    time_str += 'to ' + words[h + 1]
  return time_str