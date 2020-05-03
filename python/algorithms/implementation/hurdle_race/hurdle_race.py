def hurdle_race(k, height):
  height.sort(reverse=True)
  return max(0, height[0] - k)