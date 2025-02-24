import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)
    self.assertEqual(node, node2)

  def test_notEqTextType(self):
    node3 = TextNode("This is another text node", TextType.ITALIC, "https://www.boot.dev")
    node4 = TextNode("This is another text node", TextType.CODE, "https://boot.dev")
    self.assertNotEqual(node3, node4)

  def test_notEqText(self):
    node5 = TextNode("This is a text node", TextType.BOLD)
    node6 = TextNode("This is another text node", TextType.BOLD)
    self.assertNotEqual(node5, node6)

  def test_notEqUrl(self):
    node7 = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    node8 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
    self.assertNotEqual(node7, node8)

if __name__ == "__main__":
  unittest.main()