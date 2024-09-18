class Queue:
    """
    Class implementing QUEUE ADT.
    Supported methods are: enqueue, dequeue, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """Initialize empty queue based on Python list."""
        self._data = []

    def enqueue(self, value: object) -> None:
        """Add new element to the end of the queue."""
        self._data.append(value)

    def dequeue(self):
        """Remove element from the beginning of the queue and return its value."""
        return self._data.pop(0)

    def is_empty(self) -> bool:
        """Return True if the queue is empty, return False otherwise."""
        return len(self._data) == 0

    def __str__(self) -> str:
        """Return content of the queue as a string (for use with print)."""
        data_str = [str(item) for item in self._data]
        return "QUEUE { " + ", ".join(data_str) + " }"


class Stack:
    """
    Class implementing STACK ADT.
    Supported methods are: push, pop, top, is_empty

    DO NOT CHANGE THIS CLASS IN ANY WAY
    YOU ARE ALLOWED TO CREATE AND USE OBJECTS OF THIS CLASS IN YOUR SOLUTION
    """
    def __init__(self):
        """Initialize empty stack based on Python list."""
        self._data = []

    def push(self, value: object) -> None:
        """Add new element on top of the stack."""
        self._data.append(value)

    def pop(self):
        """Remove element from top of the stack and return its value."""
        return self._data.pop()

    def top(self):
        """Return value of top element without removing from stack."""
        return self._data[-1]

    def is_empty(self) -> bool:
        """Return True if the stack is empty, return False otherwise."""
        return len(self._data) == 0

    def __str__(self) -> str:
        """Return content of the stack as a string (for use with print)."""
        data_str = [str(item) for item in self._data]
        return "STACK: { " + ", ".join(data_str) + " }"
