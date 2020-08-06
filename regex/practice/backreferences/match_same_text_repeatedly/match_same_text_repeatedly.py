import re


def match_same_text_repeatedly(test_s):
  return str(
      bool(
          re.match(
              r'^([a-z])(\w)(\s)(\W)(\d)(\D)([A-Z])([a-zA-Z])([aeiouAEIOU])(\S)\1\2\3\4\5\6\7\8\9\10$',
              test_s))).lower()
