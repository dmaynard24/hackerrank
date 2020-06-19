from dateutil import parser


def time_delta(t1, t2):
  return str(int(abs((parser.parse(t1) - parser.parse(t2)).total_seconds())))