def text_alignment(thickness):
  c = 'H'
  result = []

  # Top Cone
  for i in range(thickness):
    result.append((c * i).rjust(thickness - 1) + c +
                  (c * i).ljust(thickness - 1))

  # Top Pillars
  for i in range(thickness + 1):
    result.append((c * thickness).center(thickness * 2) +
                  (c * thickness).center(thickness * 6))

  # Middle Belt
  for i in range((thickness + 1) // 2):
    result.append((c * thickness * 5).center(thickness * 6))

  # Bottom Pillars
  for i in range(thickness + 1):
    result.append((c * thickness).center(thickness * 2) +
                  (c * thickness).center(thickness * 6))

  # Bottom Cone
  for i in range(thickness):
    result.append(
        ((c * (thickness - i - 1)).rjust(thickness) + c +
         (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

  return result
