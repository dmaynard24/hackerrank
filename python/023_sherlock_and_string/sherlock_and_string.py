def isValid(s):
  s_chars = {}
  for s_char in list(s):
    s_chars[s_char] = s_chars.get(s_char, 0) + 1
  s_char_counts = {}
  for s_char_count in s_chars.values():
    s_char_counts[s_char_count] = s_char_counts.get(s_char_count, 0) + 1
  if len(s_char_counts) < 2:
    return 'YES'
  if len(s_char_counts) > 2:
    return 'NO'
  one, two = s_char_counts.keys()
  one_val, two_val = s_char_counts.values()
  # check to see if a single one-off char exists, if it can be removed, the string is valid
  if (one == 1 and one_val == 1) or (two == 1 and two_val == 1):
    return 'YES'
  if abs(one - two) > 1:
    return 'NO'
  if one_val != 1 and two_val != 1:
    return 'NO'
  return 'YES'


print(isValid('a'))  # 'YES'
print(isValid('aabbcd'))  # 'NO'
print(isValid('aabbccddeefghi'))  # 'NO'
print(isValid('abcdefghhgfedecba'))  # 'NO'
print(
    isValid(
        'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    ))  # 'YES'
