def taum_bday(b, w, bc, wc, z):
  return b * min(bc, wc + z) + w * min(wc, bc + z)