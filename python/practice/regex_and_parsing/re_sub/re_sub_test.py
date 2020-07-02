import unittest, re_sub


class TestReSub(unittest.TestCase):
  def test_re_sub(self):
    self.assertEqual(
        re_sub.re_sub('''a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.'''), '''a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.''')
    self.assertEqual(re_sub.re_sub('x&& &&& && && x || | ||\|| x'),
                     'x&& &&& and and x or | ||\|| x')


if __name__ == '__main__':
  unittest.main()
