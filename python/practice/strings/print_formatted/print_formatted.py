def print_formatted(n):
  mw = len(bin(n)) - 1
  result = []

  for i in range(1, n + 1):
    dec = str(i)
    octa = oct(i)[2:]
    hexa = hex(i).upper()[2:]
    bina = bin(i)[2:]
    result.append(
        dec.rjust(mw - 1) + octa.rjust(mw) + hexa.rjust(mw) + bina.rjust(mw))

  return '\n'.join(result)