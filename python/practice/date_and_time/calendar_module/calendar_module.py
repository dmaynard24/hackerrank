import calendar


def day_name(date_str):
  m, d, y = map(int, date_str.split())
  return calendar.day_name[calendar.weekday(y, m, d)].upper()