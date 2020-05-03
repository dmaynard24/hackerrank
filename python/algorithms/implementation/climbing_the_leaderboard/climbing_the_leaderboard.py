def climbing_the_leaderboard(scores, alice):
  ranks = [scores[0]]
  for i in range(1, len(scores)):
    if scores[i] < scores[i - 1]:
      ranks.append(scores[i])

  alice_ranks = []
  j = 0
  for i in range(len(ranks) - 1, -1, -1):
    while j < len(alice) and ranks[i] >= alice[j]:
      if ranks[i] > alice[j]:
        alice_ranks.append(i + 2)
      if ranks[i] == alice[j]:
        alice_ranks.append(i + 1)
      j += 1

  while j < len(alice):
    alice_ranks.append(1)
    j += 1

  return alice_ranks