import unittest, designer_pdf_viewer


class TestDesignerPdfViewer(unittest.TestCase):
  def test_designer_pdf_viewer(self):
    self.assertEqual(
        designer_pdf_viewer.designer_pdf_viewer([
            1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 5
        ], 'abc'), 9)
    self.assertEqual(
        designer_pdf_viewer.designer_pdf_viewer([
            1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
            5, 5, 5, 7
        ], 'zaba'), 28)


if __name__ == '__main__':
  unittest.main()
