import unittest, detect_html_tags


class TestDetectHtmlTags(unittest.TestCase):
  def test_detect_html_tags(self):
    self.assertEqual(
        detect_html_tags.detect_html_tags(
            '''<div id="mp-other" style="padding-top:4px; padding-bottom:2px;">
<h2><span class="mw-headline" id="Other_areas_of_Wikipedia">Other areas of Wikipedia</span></h2>
<ul>
<li><b><a href="/wiki/Wikipedia:Community_portal" title="Wikipedia:Community portal">Community portal</a></b>  Bulletin board, projects, resources and activities covering a wide range of Wikipedia areas.</li>
<li><b><a href="/wiki/Wikipedia:Help_desk" title="Wikipedia:Help desk">Help desk</a></b>  Ask questions about using Wikipedia.</li>
<li><b><a href="/wiki/Wikipedia:Local_Embassy" title="Wikipedia:Local Embassy">Local embassy</a></b>  For Wikipedia-related communication in languages other than English.</li>
<li><b><a href="/wiki/Wikipedia:Reference_desk" title="Wikipedia:Reference desk">Reference desk</a></b>  Serving as virtual librarians, Wikipedia volunteers tackle your questions on a wide range of subjects.</li>
<li><b><a href="/wiki/Wikipedia:News" title="Wikipedia:News">Site news</a></b>  Announcements, updates, articles and press releases on Wikipedia and the Wikimedia Foundation.</li>
<li><b><a href="/wiki/Wikipedia:Village_pump" title="Wikipedia:Village pump">Village pump</a></b>  For discussions about Wikipedia itself, including areas for technical issues and policies.</li>
</ul>
</div>'''), 'a;b;div;h2;li;span;ul')

  def test_detect_html_tags_1(self):
    self.assertEqual(
        detect_html_tags.detect_html_tags(
            '''<p><a href="http://www.quackit.com/html/tutorial/html_links.cfm">Example Link</a><img src="dave.png" alt="Dave" /></p>
<div class="more-info"><a href="http://www.quackit.com/html/examples/html_links_examples.cfm">More Link Examples...</a></div>'''
        ), 'a;div;img;p')


if __name__ == '__main__':
  unittest.main()
