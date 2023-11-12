class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0


    def __str__(self):
        if self.size != 0:
            cookies = ""
            for cookie in range(self.size):
                cookies += "🍪"
            return cookies
        else:
            return ""
    def deposit(self, n):
            self.size += n


    def withdraw(self, n):
            self.size -= n


    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if 0 <= size <= self.capacity:
            self._size = size
        else:
            raise ValueError


