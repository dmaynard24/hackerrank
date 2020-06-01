def second_lowest_grades(scores):
  scores.sort(key=lambda s: s[1])

  low_score = scores[0][1]
  second_lowest_scores = []
  for i in range(1, len(scores)):
    if scores[i][1] != low_score:
      second_lowest_scores.append(scores[i])
      j = i + 1
      while j < len(scores) and scores[j][1] == scores[i][1]:
        second_lowest_scores.append(scores[j])
        j += 1
      break

  if len(second_lowest_scores) > 1:
    second_lowest_scores.sort(key=lambda s: s[0])

  return [s[0] for s in second_lowest_scores]