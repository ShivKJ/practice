RED = True
BLACK = False


class Node:
    __slots__ = 'p', 'l', 'r', 'color', 'x'

    def __init__(self, x=None, color=RED):
        self.x = x
        self.p = None
        self.l = None
        self.r = None
        self.color = color

    def __str__(self):
        return str(self.x)


NIL = Node(color=BLACK)


def create_node(key) -> Node:
    '''
    Creates a new black node containing the key
    :param key:
    :return: formed Node
    '''
    node = Node(key)
    node.l = node.r = NIL
    return node


class RBTree:
    '''
    Red-Black Tree property:
            1) Every node is either red or black (always satisfied)
            2) The root is black
            3) Every leaf (NIL) is black. (always satisfied)
            4) If node is red then both it's children are black.
            5) For each node, all simple paths from the node to descendent
            leaves contain same number of black nodes.

    '''

    def __init__(self):
        self._root = NIL
        self._size = 0

    def insert(self, key):
        '''
        Inserting a node into tree. New node is created Black.
        1) Node is found where the new node(z) has to be inserted (y)
        2) This node (y) become parent of new node(z).
        3) If y is null which is case when root is null, then setting
           to root to z, otherwise it would either become left or
           right child.
        4) After inserting the node we may have violated Red-Black tree
           property, which is restored in insertion_fixup

        :param key:
        :return:
        '''
        self._size += 1

        x = self._root
        y = NIL
        z = create_node(key)

        while x is not NIL:
            y = x
            x = x.l if z.x <= x.x else x.r

        z.p = y

        if y is NIL:
            self._root = z
        elif z.x < y.x:
            y.l = z
        else:
            y.r = z

        self.insertion_fixup(z)

    def insertion_fixup(self, z: Node):
        """
        This maintains the red-black tree property after insertion of new node z
        in tree.

        If z is the root then 'while' loop is not executed as it's parent(BLACK)
        is NIL. Since root has to be black, it is set as well. Loop will also
        not be executed if z's parent is black.

        let uncle of z is son of grandparent of z who is not parent of z.
        Eg.
                        grand_parent
                        /     \
                     parent   uncle
                     /\        /\
                    z  T1     T2 T3

        Now depending upon whether uncle is left or right child, there will
        be six case. Due to symmetrical treatment we consider only three
        cases in which uncle is a right child.

        Case 1: uncle's color is Red.
            In this case, we color uncle and z's parent BLACK and
            z's grandparent RED and set z = z's grandparent. Property
            which can be violated is 2 which will be set in last line. Notice
            that if now z points to root then loop does not execute as root's
            parent is NIL color of which is black.
        Case 2: uncle's color is Black and z is right child.
            We set z = z.parent and perform left rotation wrt to z. This is
            changed to Case 3
        Case 3: uncle's color is Black and z is left child.
            We color z'parent Black and z'grandparent Red and performs right
            rotation wrt to z'parent. Note that while loop will now terminate.

        :param z: node which was inserted
        :return:
        """
        while z.p.color is RED:
            if z.p is z.p.p.l:
                # parent of z is in left.

                uncle = z.p.p.r

                if uncle.color is RED:  # case1
                    z.p.color = BLACK
                    uncle.color = BLACK

                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.r:  # case2
                        z = z.p
                        self.left_rotation(z)

                    # now starts case3
                    z.p.color = BLACK
                    z.p.p.color = RED

                    self.right_rotation(z.p.p)
            else:
                uncle = z.p.p.l

                if uncle.color is RED:
                    z.p.color = BLACK
                    uncle.color = BLACK
                    z.p.p.color = RED
                    z = z.p.p
                else:
                    if z is z.p.l:
                        z = z.p
                        self.right_rotation(z)
                    z.p.color = BLACK
                    z.p.p.color = RED
                    self.left_rotation(z.p.p)

        self._root.color = BLACK

    def left_rotation(self, x: Node):
        y = x.r
        x.r = y.l
        '''
                    |                               |
                    x                               y
                   / \           L(x)              / \
                  A   y        -------->          x   G
                     / \                         / \
                    B   G                       A   B
        '''

        if y.l is not NIL:
            y.l.p = x

        y.p = x.p

        if x.p is NIL:
            self._root = y
        elif x is x.p.l:
            x.p.l = y
        else:
            x.p.r = y

        y.l = x
        x.p = y

    def right_rotation(self, y: Node):
        x = y.l

        '''
                    |                               |
                    y                               x
                   / \           R(y)              / \
                  x   G        ------>            A   y    
                 / \                                 / \
                A   B                               B   G
        '''

        y.l = x.r

        if x.r is not NIL:
            x.r.p = y

        x.p = y.p

        if y.p is NIL:
            self._root = x
        elif y is y.p.l:
            y.p.l = x
        else:
            y.p.r = x

        x.r = y
        y.p = x

    @staticmethod
    def _pre_order(node: Node):
        if node.l is not NIL:
            RBTree._pre_order(node.l)

        print(node.x)

        if node.r is not NIL:
            RBTree._pre_order(node.r)

    def pre_order(self):
        if self._root is not NIL:
            RBTree._pre_order(self._root)
        else:
            print('No Nodes')

    @staticmethod
    def _height(n: Node):
        return 0 if n is NIL or n.l is n.r else 1 + max(RBTree._height(n.l),
                                                        RBTree._height(n.r))

    def height(self):
        return RBTree._height(self._root)

    @staticmethod
    def _internal_nodes(n: Node):
        if n.l is n.r:
            return 0
        return 1 + RBTree._internal_nodes(n.l) + RBTree._internal_nodes(n.r)

    def internal_nodes(self):
        return RBTree._internal_nodes(self._root)

    @staticmethod
    def _external_node(n: Node):
        if n is NIL:
            return 0

        if n.l is n.r:
            return 1

        return RBTree._external_node(n.l) + RBTree._external_node(n.r)

    def external_node(self):
        return RBTree._external_node(self._root)

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._root is not NIL

    @staticmethod
    def tree_min(n: Node):
        while n.left is not NIL:
            n = n.left

        return n

    def transplant(self, u: Node, v: Node):
        """
        Replaces node u with node v.
        :param u:
        :param v:
        :return:
        """

        if u.p is NIL:
            self._root = v
        elif u is u.p.l:
            u.p.l = v
        else:
            u.p.r = v

        if v is not NIL:
            v.p = u.p

    def delete(self, z: Node):

        y_col = z.color

        if z.l is NIL:
            x = z.r
            self.transplant(z, x)
        elif z.r is NIL:
            x = z.l
            self.transplant(z, x)
        else:
            y = RBTree.tree_min(z.r)
            y_col = y.color
            x = y.r

            if y.p is z:
                x.p = z
            else:
                self.transplant(y, x)
                y.r = z.r
                z.r.p = y

            self.transplant(z, y)

            y.l = z.l
            z.l.p = y

            y.color = z.color

        if y_col is BLACK:
            self.deletion_fixup(x)

    def deletion_fixup(self, x: Node):
        while x is not self._root and x.color is BLACK:
            if x is x.p.l:
                w = x.p.r
                if w.color is RED:
                    w.color = BLACK
                    x.p.color = RED
                    self.left_rotation(x.p)
                    w = x.p.r
                if w.l.color is w.r.color is BLACK:
                    w.color = RED
                    x = x.p
                else:
                    if w.r.color is BLACK:
                        w.l.color = BLACK
                        w.color = RED
                        self.right_rotation(w)
                        w = x.p.r

                    w.color = x.p.color
                    x.p.color = w.r.color = BLACK
                    self.left_rotation(x.p)
                    x = self._root
            else:
                # TODO
                pass

        x.color = BLACK
