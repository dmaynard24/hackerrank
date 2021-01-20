import re


def get_email_addresses(s):
  return ';'.join(sorted(set(re.findall(r'[\w\.]+@[\w+\.]+\.\w+', s))))