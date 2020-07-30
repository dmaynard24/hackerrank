import unittest, get_programming_lang


class TestGetProgrammingLang(unittest.TestCase):
  def test_get_programming_lang(self):
    self.assertEqual(
        get_programming_lang.get_programming_lang('''import java.io.*;

public class SquareNum {

   public static void main(String args[]) throws IOException
   {
      System.out.println("This is a small Java Program!");
   }
}'''), 'Java')

  def test_get_programming_lang_1(self):
    self.assertEqual(
        get_programming_lang.get_programming_lang(
            '''# let us create a test string
testString1 = "Hello World!"
print "Original String: "+ testString1
# Print this string in lower case
# Converting a string to lower case
print "Converting to LowerCase"
print testString1.lower()
# Converting a string to upper case
print "Converting to Upper Case"
print testString1.upper()
# Capitalizing a string'''), 'Python')


if __name__ == '__main__':
  unittest.main()
