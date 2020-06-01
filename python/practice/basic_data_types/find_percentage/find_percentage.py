def find_percentage(student_marks, query_name):
  return '{:.2f}'.format(
      sum(student_marks[query_name]) / len(student_marks[query_name]))
