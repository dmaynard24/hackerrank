def acm_team(topic):
  max_topics = 0
  max_topics_count = 0
  for i in range(len(topic) - 1):
    team_one = list(topic[i])
    for j in range(i + 1, len(topic)):
      team_two = list(topic[j])
      topics = 0
      for k in range(len(team_one)):
        if team_one[k] == '1' or team_two[k] == '1':
          topics += 1
      if topics > max_topics:
        max_topics = topics
        max_topics_count = 1
      elif topics == max_topics:
        max_topics_count += 1
  return [max_topics, max_topics_count]