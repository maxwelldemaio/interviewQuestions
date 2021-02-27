class Node:
    def __init__(self, data=None, next=None):
        # Value and pointer(to a Node)
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beg(self, data):
        """Insert node at beg of LL"""
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr = self.head
        llstr = ''
        # Traverse
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        """Insert node at end of LL"""
        # Insert at beginning if empty
        if self.head is None:
            self.head = Node(data, None)
            return

        # Iterate to the end and add Node
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        """Take list of values and make LL"""
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """Get length of LL"""
        counter = 0
        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_at(self, index):
        """Remove element at given index"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        # Remove head, just move pointer to next
        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        """Insert node at given index"""
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_beg(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            count += 1
            itr = itr.next

    def insert_after_value(self, data_after, data_to_insert):
        """Insert data after data criteria encountered"""
        count = 0
        iter = self.head
        while iter:
            if iter.data == data_after:
                self.insert_at(count + 1, data_to_insert)
            count += 1
            iter = iter.next

    def remove_by_value(self, data):
        """Remove first node that contains data"""
        count = 0
        iter = self.head
        while iter:
            if iter.data == data:
                self.remove_at(count)
            count += 1
            iter = iter.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print()
    ll.insert_after_value("mango", "apple")  # insert apple after mango
    ll.print()
    ll.remove_by_value("orange")  # remove orange from linked list
    ll.print()
    ll.remove_by_value("figs")
    ll.print()
    ll.remove_by_value("banana")
    ll.remove_by_value("mango")
    ll.remove_by_value("apple")
    ll.remove_by_value("grapes")
    ll.print()
