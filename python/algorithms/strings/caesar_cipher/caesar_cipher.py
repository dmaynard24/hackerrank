def caesar_cipher(s, k):
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