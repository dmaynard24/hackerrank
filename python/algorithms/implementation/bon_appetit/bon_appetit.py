def bon_appetit(bill, k, b):
  expected_share = (sum(bill) - bill[k]) // 2
  if b == expected_share:
    return 'Bon Appetit'
  else:
    return b - expected_share
