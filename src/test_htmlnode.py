import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )
        self.assertEqual(
            node.tag,
            "a",
        )
        self.assertEqual(
            node.value,
            "Click me!",
        )
        self.assertEqual(
            node.props,
            {"href": "https://www.google.com"},
        )

    def test_values(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(
            node.value,
            "This is a paragraph of text.",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
      node = ParentNode(
          "p",
          [
              LeafNode("b", "Bold text"),
              LeafNode(None, "Normal text"),
              LeafNode("i", "italic text"),
              LeafNode(None, "Normal text"),
          ],
      )
      self.assertEqual(
          node.to_html(),
          '<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
      )



if __name__ == "__main__":
    unittest.main()
