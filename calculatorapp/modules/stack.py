class Stack:
    """
    A simple stack implementation.

    Author: Stephen Tse <***@cmu.edu>
    Version: 1.1.0
    """

    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def parse(self, stack_string):
        """
        Parse a stack string produced by the overridden __repr__
        method below (format: a b c ...) and assign its value
        to the current stack, overwritting existing content.

        Function returns a boolean value indicating if the string
        contains valid stack content
        """
        # don't use delimeters other than the default space, because
        # str.split() will not return an empty list (more specifically,
        # it will return ['']) on an empty string if a delimeter
        # argument is provided to split()
        temp = stack_string.split()
        if not temp:  # if stack is empty, then nothing to be done
            return False
        else:
            self.items.clear()
            try:  # is this the operand stack?
                self.items += [int(i) for i in temp]
            except ValueError:  # nope, this probably is the operator stack
                self.items += temp
            # TODO: Will the '+=' operator in python appends items in list
            # temp to the current items list, or will it create a copy of
            # items before concatenation? If it's the latter, then there's no
            # point in clearing old list then using '+=' at all, because I only
            # want to reuse existing objects.
            return True

    def __str__(self):
        return ' '.join(str(s) for s in self.items)
