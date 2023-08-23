class Doubly_Linked_List_Node:
    def __init__(self, x):
        self.item = x
        self.prev = None
        self.next = None

    def later_node(self, i):
        if i == 0: return self
        assert self.next
        return self.next.later_node(i - 1)

class Doubly_Linked_List_Seq:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
        return '-'.join([('(%s)' % x) for x in self])

    def build(self, X):
        for a in X:
            self.insert_last(a)

    def get_at(self, i):
        node = self.head.later_node(i)
        return node.item

    def set_at(self, i, x):
        node = self.head.later_node(i)
        node.item = x

    def insert_first(self, x):
        new_node = Doubly_Linked_List_Node(x)
        head = self.head
        if not head:
            self.head = self.tail = new_node
            return
        self.head = new_node
        new_node.next = head
        head.prev = new_node

    def insert_last(self, x):
        new_node = Doubly_Linked_List_Node(x)
        tail = self.tail
        if not tail:
            self.head = self.tail = new_node
            return
        self.tail = new_node
        new_node.prev = tail
        tail.next = new_node

    def delete_first(self):
        del_head = self.head
        assert del_head
        x = del_head.item
        if self.head == self.tail:
            self.head = self.tail = None
            del del_head
            return x
        self.head = del_head.next
        self.head.prev = None
        del del_head        
        return x

    def delete_last(self):
        del_tail = self.tail
        assert del_tail
        x = del_tail.item
        if self.head == self.tail:
            self.head = self.tail = None
            del del_tail
            return x
        self.tail = del_tail.prev
        self.tail.next = None
        del del_tail   
        return x

    def remove(self, x1, x2):
        L2 = Doubly_Linked_List_Seq()
        if x1 == self.head:
            self.head = x2.next
        else: 
            x1.prev.next = x2.next

        if x2 == self.tail:
            self.tail = x1.prev
        else:
            x2.next.prev = x1.prev
        L2.head = x1
        L2.tail = x2
        x1.prev = x2.next = None
        return L2

    def splice(self, x, L2):
        x_n = x.next
        x_1, x_2 = L2.head, L2.tail
        x.next = x_1
        x_1.prev = x
        x_2.next = x_n
        L2.head = L2.tail = None
        if not x_n:
            self.tail = x_2
        else:
            x_n.prev = x_2   