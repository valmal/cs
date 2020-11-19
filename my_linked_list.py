class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def is_tail(self):
        return self.next == None

class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def is_valid_index(self, index):
        return not (index > self.size - 1 or index < 0)

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        self.size += 1
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        self.add(val)

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended
        to the end of linked list. If index is greater than the length,
        the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index != self.size and not self.is_valid_index(index):
            return

        if index == 0:
            return self.addAtHead(val)

        if index == self.size:
            return self.addAtTail(val)
        elif index < self.size:
            self.size += 1
            current_node = self.head
            current_index = 0
            while current_node:
                if current_index == index - 1:
                    break
                current_node = current_node.next
                current_index += 1
            new_node = Node(val)
            new_node.next = current_node.next
            current_node.next = new_node

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if not self.is_valid_index(index):
            return

        if index == 0:
            if self.head == self.tail:
                self.tail = self.tail.next
            self.head = self.head.next

        elif index == self.get_size() - 1:
            current_node = self.head
            current_index = 0
            while current_node:
                if current_index == index - 1:
                    current_node.next = None
                    self.tail = current_node
                    break
                current_node = current_node.next
                current_index += 1
        else:
            current_node = self.head
            current_index = 0
            while current_node:
                if current_index == index - 1:
                    current_node.next = current_node.next.next
                    break
                current_node = current_node.next
                current_index += 1

        self.size -= 1

    def get(self, index) :
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        print('Get on ' + str(index) + ' size = ' + str(self.size))
        if not self.is_valid_index(index):
            return -1

        current_node = self.head
        current_index = 0
        while current_node:
            if current_index == index:
                return current_node.val
            current_node = current_node.next
            current_index += 1

    def get_slow(self, index):
        if self.is_valid_index(index):
            return self.to_list()[index]
        else:
            return -1

    def to_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return result

    def p(self):
        current_node = self.head
        while current_node:
            print(current_node.val)
            current_node = current_node.next

    def add(self, val):
        new_node = Node(val)
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def get_size(self):
        return self.size
