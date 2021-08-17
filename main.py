class MyReverse:

    def __init__(self, list):
        self.list = list

    def __iter__(self):
        return self

    def __next__(self):
        for item in range(self.list):
            return item

    def __reversed__(self):
        for item in self.list[::-1]:
            return item


a = MyReverse([1, 2, 3])
print(reversed(a))
