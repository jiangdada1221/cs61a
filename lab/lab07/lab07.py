""" Lab 07: Recursive Objects """

# Q4
def link_to_list(link):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    new_list = []
    if link is Link.empty:
        return []
    else:
        return [link.first] + link_to_list(link.rest)


# Q5
def store_digits(n):
    """Stores the digits of a positive number n in a linked list.

    >>> s = store_digits(1)
    >>> s
    Link(1)
    >>> store_digits(2345)
    Link(2, Link(3, Link(4, Link(5))))
    >>> store_digits(876)
    Link(8, Link(7, Link(6)))
    """
    link = Link(n % 10)
    n = n // 10
    while n != 0:
        link = Link(n% 10, link)
        n = n // 10
    return link




# Q6
def cumulative_sum(t):
    """Mutates!! t so that each node's label becomes the sum of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_sum(t)
    >>> t
    Tree(16, [Tree(8, [Tree(5)]), Tree(7)])
    """
    if t.is_leaf():
        t.label = t.label
    # else:
    #     t.label = max[cumulative_sum(b).label for b in t.branches]  because 这个method是不return的 只是改变attributes 所以会报错
    else:
        sum = 0
        for b in t.branches:
            cumulative_sum(b)
            sum += b.label
        t.label += sum

# Q7
def is_bst(t):
    """Returns True if the Tree t has the structure of a valid BST.

    >>> t1 = Tree(6, [Tree(2, [Tree(1), Tree(4)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t1)
    True
    >>> t2 = Tree(8, [Tree(2, [Tree(9), Tree(1)]), Tree(3, [Tree(6)]), Tree(5)])
    >>> is_bst(t2)
    False
    >>> t3 = Tree(6, [Tree(2, [Tree(4), Tree(1)]), Tree(7, [Tree(7), Tree(8)])])
    >>> is_bst(t3)
    False
    >>> t4 = Tree(1, [Tree(2, [Tree(3, [Tree(4)])])])
    >>> is_bst(t4)
    True
    >>> t5 = Tree(1, [Tree(0, [Tree(-1, [Tree(-2)])])])
    >>> is_bst(t5)
    True
    >>> t6 = Tree(1, [Tree(4, [Tree(2, [Tree(3)])])])
    >>> is_bst(t6)
    True
    >>> t7 = Tree(2, [Tree(1, [Tree(5)]), Tree(4)])
    >>> is_bst(t7)
    False
    """
    if len(t.branches) > 2:      #this one is really hard
        return False
    if t.is_leaf():
        return True
    if len(t.branches) == 1 and is_bst(t.branches[0]):
        if t.branches[0].label <= t.label:
            return t.label >= bst_max(t.branches[0])
        else:
            return t.label < bst_min(t.branches[0])
    if is_bst(t.branches[0]) and is_bst(t.branches[1]):
        return t.label >= bst_max(t.branches[0]) and t.label < bst_min(t.branches[1])
    return False

def bst_max(bt):
    if not bt.branches:
        return bt.label
    elif len(bt.branches) == 2:
        return bst_max(bt.branches[1])
    else:
        if bt.label >= bt.branches[0].label:
            return bt.label
        else:
            return bst_max(bt.branches[0])
def bst_min(bt):
    if not bt.branches:
        return bt.label
    elif len(bt.branches) == 2:
        return bst_min(bt.branches[0])
    else:
        if bt.label >= bt.branches[0].label :
            return bst_min(bt.branches[0])
        else:
            return bt.label



# Q8

def in_order_traversal(t):   #veryvery difficult
    """
    Generator function that generates an "in-order" traversal, in which we
    yield the value of every node in order from left to right, assuming that each node has either 0 or 2 branches.

    For example, take the following tree t:
            1
        2       3
    4     5
         6  7

    We have the in-order-traversal 4, 2, 6, 5, 7, 1, 3

    >>> t = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(6), Tree(7)])]), Tree(3)])
    >>> list(in_order_traversal(t))
    [4, 2, 6, 5, 7, 1, 3]
    """
    if t.is_leaf():
        yield t.label
    else:
        t.left,t.right = in_order_traversal(t.branches[0]),in_order_traversal(t.branches[1])
        yield from t.left
        yield t.label
        yield from t.right
        #先考虑    2-1，3  然后这个2-1，3成为一个整体，yield from 后list是一次性全部yield出来
#                也就是一个迭代  考虑这个呢  假设inordr函数的左边支是yield对的，那么只需接着yield label 在yield右边支即可





# Linked List Class
class Link:
    """A linked list.

    >>> s = Link(1)
    >>> s.first
    1
    >>> s.rest is Link.empty
    True
    >>> s = Link(2, Link(3, Link(4)))
    >>> s.second
    3
    >>> s.first = 5
    >>> s.second = 6
    >>> s.rest.rest = Link.empty
    >>> s                                    # Displays the contents of repr(s)
    Link(5, Link(6))
    >>> s.rest = Link(7, Link(Link(8, Link(9))))
    >>> s
    Link(5, Link(7, Link(Link(8, Link(9)))))
    >>> print(s)                             # Prints str(s)
    <5 7 <8 9>>
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    @property
    def second(self):
        return self.rest.first

    @second.setter
    def second(self, value):
        self.rest.first = value


    def __repr__(self):
        if self.rest is not Link.empty:
            rest_repr = ', ' + repr(self.rest)
        else:
            rest_repr = ''
        return 'Link(' + repr(self.first) + rest_repr + ')'

    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

# Tree Class
class Tree:
    """
    >>> t = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
    >>> t.label
    3
    >>> t.branches[0].label
    2
    >>> t.branches[1].is_leaf()
    True
    """
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = list(branches)

    def is_leaf(self):
        return not self.branches

    def map(self, fn):
        """
        Apply a function `fn` to each node in the tree and mutate the tree.

        >>> t1 = Tree(1)
        >>> t1.map(lambda x: x + 2)
        >>> t1.map(lambda x : x * 4)
        >>> t1.label
        12
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> t2.map(lambda x: x * x)
        >>> t2
        Tree(9, [Tree(4, [Tree(25)]), Tree(16)])
        """
        self.label = fn(self.label)
        for b in self.branches:
            b.map(fn)

    def __contains__(self, e):
        """
        Determine whether an element exists in the tree.

        >>> t1 = Tree(1)
        >>> 1 in t1
        True
        >>> 8 in t1
        False
        >>> t2 = Tree(3, [Tree(2, [Tree(5)]), Tree(4)])
        >>> 6 in t2
        False
        >>> 5 in t2
        True
        """
        if self.label == e:
            return True
        for b in self.branches:
            if e in b:
                return True
        return False

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        def print_tree(t, indent=0):
            tree_str = '  ' * indent + str(t.label) + "\n"
            for b in t.branches:
                tree_str += print_tree(b, indent + 1)
            return tree_str
        return print_tree(self).rstrip()
def split(n):
    list = []
    if n < 10:
        return [n]
    else:
        list = split(n // 10) + [n % 10]
    return list
