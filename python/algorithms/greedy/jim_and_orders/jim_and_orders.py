from functools import cmp_to_key


def jim_and_orders(orders):
  def comparator(a, b):
    if a['time'] < b['time']:
      return -1
    elif a['time'] > b['time']:
      return 1
    else:
      if a['number'] < b['number']:
        return -1
      else:
        return 1

  order_times = [{
      'number': i + 1,
      'time': order[0] + order[1]
  } for i, order in enumerate(orders)]
  order_times.sort(key=cmp_to_key(comparator))

  return [order_time['number'] for order_time in order_times]