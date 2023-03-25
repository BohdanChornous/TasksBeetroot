from bs4 import BeautifulSoup
from html.parser import HTMLParser


class Node:
    def __init__(self, tag, text=None):
        self.tag = tag
        self.text = text
        self.parent = None
        self.children = []

    def add_children(self, node):
        self.children.append(node)
        node.parent = self

    def find_by_tag(self, tag):
        if self.tag == tag:
            return self.text
        else:
            for child in self.children:
                text = child.find_by_tag(tag)
                if text is not None:
                    return text
        return None


class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.my_tree = None

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if self.my_tree is None:
            self.my_tree = Node(tag)
        else:
            node = Node(tag)
            self.my_tree.add_children(node)
            self.my_tree = node

    def handle_endtag(self, tag: str) -> None:
        if self.my_tree.parent is not None:
            self.my_tree = self.my_tree.parent

    def handle_data(self, data: str) -> None:
        if self.my_tree:
            self.my_tree.text = repr(data)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        node = Node(tag)
        self.my_tree.add_children(node)

    def build_tree(self, html):
        with open(html) as f:
            file_html = f.read()
        parser.feed(file_html)
        tree = self.my_tree
        self.my_tree = None
        return tree

# try 2


def print_tree(node, level=0):
    print(f"{level * ' '}{node.tag} -> {node.text}")
    for child in node.children:
        print_tree(child, level + 2)


def find_parent(dad, teg):
    if len(dad.children) == 0:
        return dad
    for child in dad.children:
        my = teg.parent.name
        n = child.tag
        if n == my:
            return child
    return find_parent(dad.parent, teg)


def build_tree_bs4(html):
    with open(html) as file:
        soup = BeautifulSoup(file, 'html.parser')
    root = Node(soup.name)
    current_root = root
    for teg in soup.find_all():
        tag_name = teg.name
        if teg.string:
            tag_text = teg.string
        else:
            tag_text = None
        node_children = Node(tag_name, tag_text)
        current_root = find_parent(current_root, teg)
        current_root.add_children(node_children)
    return root


my_html_root = build_tree_bs4('les27.html')
parser = MyHTMLParser()
my_tree = parser.build_tree('les27.html')
print_tree(my_tree)
print(my_tree.find_by_tag("em"))
