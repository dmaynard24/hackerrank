# Plus Minus

# Given an array of integers, calculate the fractions of its elements that are positive, negative, and are zeros. Print the decimal value of each fraction on a new line.

# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.

# For example, given the array arr = [1, 1, 0, -1, -1] there are 5 elements, two positive, two negative and one zero. Their ratios would be 2/5 = 0.4, 2/5 = 0.4 and 1/5 = 0.2. It should be returned as

# [0.4, 0.4, 0.2]

# Function Description

# Complete the plus_minus function in the editor below. It should return the ratio of positive, negative and zero items in the array, each on a separate line rounded to six decimals.

# plus_minus has the following parameter(s):

# arr: an array of integers
# Input Format

# The first line contains an integer, n, denoting the size of the array.
# The second line contains n space-separated integers describing an array of numbers.

# Constraints
# 0 < n <= 100
# -100 <= arr[i] <= 100

# Output Format

# You must return the following:

# A decimal representing of the fraction of positive numbers in the array compared to its size.
# A decimal representing of the fraction of negative numbers in the array compared to its size.
# A decimal representing of the fraction of zeros in the array compared to its size.

# Sample Input
# 6
# -4 3 -9 0 4 1

# Sample Output
# [0.5, 0.3333333333333333, 0.16666666666666666]

# Explanation
# There are 3 positive numbers, 2 negative numbers, and 1 zero in the array.
# The proportions of occurrence are positive: 3/6 = 0.5, negative: 2/6 = 0.3333333333333333 and zeros: 1/6 = 0.16666666666666666.


def plus_minus(arr):
  pos_count = 0
  neg_count = 0
  zero_count = 0
  for num in arr:
    if num > 0:
      pos_count += 1
    elif num < 0:
      neg_count += 1
    else:
      zero_count += 1
  length = len(arr)
  return [pos_count / length, neg_count / length, zero_count / length]
