def designer_pdf_viewer(h, word):
  height = 0
  chars = list(word)
  for char in chars:
    height = max(height, h[ord(char) - 97])
  return height * len(word)