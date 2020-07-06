from io import StringIO
from unittest.mock import patch
import unittest, html_parser_1


class TestHtmlParser1(unittest.TestCase):
  def test_html_parser_1(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      html_parser_1.html_parser_1(
          '''<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>''')
      self.assertEqual(
          fake_out.getvalue(), '''Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html
''')

  def test_html_parser_1_longer(self):
    with patch('sys.stdout', new=StringIO()) as fake_out:
      html_parser_1.html_parser_1('''<article class="hentry">
    <!-- <header>
      <h1 class="entry-title">But Will It Make You Happy?</h1>
      <time class="updated" datetime="2010-08-07 11:11:03-0400">08-07-2010</time>
      <p class="byline author vcard">
          By <span class="fn">Stephanie Rosenbloom</span>
      </p>
    </header> -->

    <div class="entry-content">
        <p>...article text...</p>
        <p>...article text...</p>

        <figure>
          <img src="tammy-strobel.jpg" alt="Portrait of Tammy Strobel" />
          <figcaption>Tammy Strobel in her pared-down, 400sq-ft apt.</figcaption>
        </figure>

        <p>...article text...</p>
        <p>...article text...</p>

        <aside>
          <h2>Share this Article</h2>
          <ul>
            <li>Facebook</li>
            <li>Twitter</li>
            <li>Etc</li>
          </ul>
        </aside>

        <div class="entry-content-asset">
          <a href="photo-full.png">
            <img src="photo.png" alt="The objects Tammy removed from her life after moving" />
          </a>
        </div>

        <p>...article text...</p>
        <p>...article text...</p>

        <a class="entry-unrelated" href="http://fake.site/">Find Great Vacations</a>
    </div>

    <footer>
      <p>
        A version of this article appeared in print on August 8,
        2010, on page BU1 of the New York edition.
      </p>
      <div class="source-org vcard copyright">
          Copyright 2010 <span class="org fn">The New York Times Company</span>
      </div>
    </footer>
  </article>''')
      self.assertEqual(
          fake_out.getvalue(), '''Start : article
-> class > hentry
Start : div
-> class > entry-content
Start : p
End   : p
Start : p
End   : p
Start : figure
Empty : img
-> src > tammy-strobel.jpg
-> alt > Portrait of Tammy Strobel
Start : figcaption
End   : figcaption
End   : figure
Start : p
End   : p
Start : p
End   : p
Start : aside
Start : h2
End   : h2
Start : ul
Start : li
End   : li
Start : li
End   : li
Start : li
End   : li
End   : ul
End   : aside
Start : div
-> class > entry-content-asset
Start : a
-> href > photo-full.png
Empty : img
-> src > photo.png
-> alt > The objects Tammy removed from her life after moving
End   : a
End   : div
Start : p
End   : p
Start : p
End   : p
Start : a
-> class > entry-unrelated
-> href > http://fake.site/
End   : a
End   : div
Start : footer
Start : p
End   : p
Start : div
-> class > source-org vcard copyright
Start : span
-> class > org fn
End   : span
End   : div
End   : footer
End   : article
''')


if __name__ == '__main__':
  unittest.main()
