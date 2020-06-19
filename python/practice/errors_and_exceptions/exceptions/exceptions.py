def exceptions(a, b):
  try:
    a, b = int(a), int(b)
    return a // b
  except (ValueError, ZeroDivisionError) as error:
    return f'Error Code: {error}'