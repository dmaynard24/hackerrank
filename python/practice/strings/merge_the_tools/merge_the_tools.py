def merge_the_tools(string, k):
  subs = []
  for i in range(0, len(string), k):
    sub = string[i:i + k]
    new_sub = ''
    sub_chars = {}
    for char in sub:
      if char not in sub_chars:
        new_sub += char
      sub_chars[char] = 1
    subs.append(new_sub)
  return '\n'.join(subs)