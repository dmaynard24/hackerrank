def alternate(s):
  def remove_adj(st):
    # remove adjacent chars (all instances, repeatedly)
    i = 0
    while len(st) > 0 and i < len(st) - 1:
      if st[i] == st[i + 1]:
        st = st.replace(st[i], '')
        i = 0
      else:
        i += 1
    return st

  def is_alternating(st):
    if len(st) < 2:
      return False
    if len(st) == 2:
      return st[0] != st[1]
    for i in range(2, len(st)):
      if st[i] != st[i - 2] or st[i] == st[i - 1]:
        return False
    return True

  max_len = [0]

  def get_alternate_len(st):
    if is_alternating(st):
      max_len[0] = max(max_len[0], len(st))
      return len(st)

    st = remove_adj(st)
    chars = {char: 1 for char in st}
    char_count = len(chars)

    if char_count <= 1:
      return 0
    elif char_count == 2:
      if is_alternating(st):
        max_len[0] = max(max_len[0], len(st))
        return len(st)
      else:
        return 0
    else:
      for char in chars.keys():
        new_str = st.replace(char, '')
        if len(new_str) >= max_len[0]:
          get_alternate_len(new_str)

  get_alternate_len(s)

  return max_len[0]


# print(alternate('asdcbsdcagfsdbgdfanfghbsfdab'))  # 8


def caesarCipher(s, k):
  encoded = ''
  for char in s:
    char_code = ord(char)
    if char_code >= 65 and char_code <= 90:
      encoded += chr(((char_code - 65 + k) % 26) + 65)
    elif char_code >= 97 and char_code <= 122:
      encoded += chr(((char_code - 97 + k) % 26) + 97)
    else:
      encoded += char
  return encoded


# print(caesarCipher('middle-Outz', 2))
print(caesarCipher('Hello_World!', 4))

print(ord('z'))