import re


def get_ip_address_type(s):
  ipv4_section = '([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])'
  ipv6_section = '[0-9a-f]{1,4}'

  if bool(re.match(r'^(%s\.){3}%s$' % (ipv4_section, ipv4_section), s)):
    return 'IPv4'
  elif bool(re.match(r'^(%s:){7}%s$' % (ipv6_section, ipv6_section), s)):
    return 'IPv6'
  else:
    return 'Neither'