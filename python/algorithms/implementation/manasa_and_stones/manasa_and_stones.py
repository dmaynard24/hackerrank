def manasa_and_stones(n, a, b):
  return sorted(list({(n - i - 1) * a + i * b for i in range(n)}))


# print(stones(3, 1, 2))  # [2, 3, 4]
# print(stones(4, 10, 100))  # [30, 120, 210, 300]
# print(stones(5, 3, 23))  # [12, 32, 52, 72, 92]
# print(
#     stones(12, 73,
#            82))  # [803, 812, 821, 830, 839, 848, 857, 866, 875, 884, 893, 902]
