class Node:
    def __init__(self, date):
        self.left = None
        self.right = None
        self.date = date


class Tree:
    def __init__(self):
        self.root = None

    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value == node.date:
            return node, parent, True

        if value < node.date:
            if node.left:
                return self.__find(node.left, node, value)

        if value > node.date:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    def insert(self, obj):

        if self.root is None:
            self.root = obj
            return obj

        s, p, flag_find = self.__find(self.root, None, obj.date)

        if not flag_find and s:
            if obj.date < s.date:
                s.left = obj
            else:
                s.right = obj
        return obj

    @staticmethod
    def __del_leaf(s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None

    @staticmethod
    def __del_one_child(s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left

    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent

    def remove(self, key):

        s, p, flag_find = self.__find(self.root, None, key)

        if not flag_find:
            return None
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.date = sr.date
            self.__del_one_child(sr, pr)

    def _print_tree_2d(self):
        my_root = self.root

        def height(my_root):
            return 1 + max(height(my_root.left), height(my_root.right)) if my_root else -1

        nlevels = height(my_root)
        width = pow(2, nlevels + 1)

        q = [(my_root, 0, width, 'c')]
        levels = []

        while (q):
            node, level, x, align = q.pop(0)
            if node:
                if len(levels) <= level:
                    levels.append([])

                levels[level].append([node, level, x, align])
                seg = width // (pow(2, level + 1))
                q.append((node.left, level + 1, x - seg, 'l'))
                q.append((node.right, level + 1, x + seg, 'r'))

        for i, l in enumerate(levels):
            pre = 0
            preline = 0
            linestr = ''
            pstr = ''
            seg = width // (pow(2, i + 1))
            for n in l:
                valstr = str(n[0].date)
                if n[3] == 'r':
                    linestr += ' ' * (n[2] - preline - 1 - seg - seg // 2) + '¯' * (seg + seg // 2) + '\\'
                    preline = n[2]
                if n[3] == 'l':
                    linestr += ' ' * (n[2] - preline - 1) + '/' + '¯' * (seg + seg // 2)
                    preline = n[2] + seg + seg // 2
                pstr += ' ' * (n[2] - pre - len(valstr)) + valstr  # correct the potition acording to the number size
                pre = n[2]
            print(linestr)
            print(pstr)

    def print_tree(self, node):
        if node is None:
            return

        self.print_tree(node.left)
        print(node.date)
        self.print_tree(node.right)


v = [10, 5, 7, 16, 13, 2, 20, 25, 19]

myTree = Tree()

for x in v:
    myTree.insert(Node(x))

myTree.print_tree(myTree.root)
myTree._print_tree_2d()
myTree.remove(16)
myTree._print_tree_2d()

p = myTree.root
v = [p]

while v:
    vn = []
    for x in v:
        print(x.date)
        if x.left:
            vn += [x.left]
        if x.right:
            vn += [x.right]
    v = vn
