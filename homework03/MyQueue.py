class Node:

    def __init__(self, contained_object, next_object):

        self.contained_object = contained_object
        self.next_object = next_object


    def __str__(self):
        return f"Node({self.contained_object})"


class MyQueue:

    length = 0

    def __init__(self):
        self.head = None

    def add(self, data):
        self.length += 1

        current = self.head

        new_object = Node(data, None)

        if current is None:
            self.head = new_object
            return



        while current.next_object is not None:
            current = current.next_object

        current.next_object = new_object


    def pop(self) -> Node:
        self.length -= 1

        head = self.head

        if head is None:
            raise ValueError("The my_queue is empty. You can not delete an element.")

        previous_head = self.head
        self.head = head.next_object

        return previous_head

    def remove(self, index: int) -> Node:
        if index >= self.length:
            raise ValueError(f"You can not delete an element with such index: '{index}', "
                             f"while length is '{self.length}'")

        current_index = 0

        current = self.head

        if index == 0:
            return self.pop()

        self.length -= 1

        while current_index < index - 1:
            current = current.next_object

            current_index += 1


        to_delete = current.next_object
        current.next_object = to_delete.next_object

        return current



    def clear(self):
        self.head = None
        self.length = 0

    def __str__(self):
        res = []

        current = self.head

        while current is not None:
            res.append(str(current.contained_object))
            current = current.next_object


        return '[' + ', '.join(res) + ']'
