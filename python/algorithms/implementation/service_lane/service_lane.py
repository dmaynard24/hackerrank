def service_lane(width, cases):
  return [min(width[case[0]:case[1] + 1]) for case in cases]
