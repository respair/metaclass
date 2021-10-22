"""list"""

class NewList(list):
    """list with advanced features"""

    def __init__(self, arr=None):
        """constructor"""
        if arr is None:
            arr = []
        self.list = arr
        self.len = len(arr)

    def append(self, item):
        """adding an element to the end"""
        self.list.append(item)
        self.len = len(self.list)

    def copy(self, arr):
        """copy one array to another"""
        self.list = []
        for i in range(len(arr)):
            self.list.append(arr[i])
        self.len = len(self.list)

    def new_size_list(self, other):
        """creating a list based on the original one
        with the addition of zeros"""
        list_time = self.list[:]
        if self.len < len(other):
            i = self.len
            while i < len(other):
                list_time.append(0)
                i += 1
        return NewList(list_time)

    def __len__(self):
        """overriding the method to get the length of the list"""
        return self.len

    def __add__(self, other):
        """redefining the + operator"""
        list_time = self.new_size_list(other)
        for j in range(len(other)):
            list_time.list[j] = list_time.list[j] + other[j]
        return list_time

    __radd__ = __add__

    def __sub__(self, other):
        """redefining the - operator"""
        list_time = self.new_size_list(other)
        for j in range(len(other)):
            list_time.list[j] = list_time.list[j] - other[j]
        return list_time

    def inverse_sub(self, other):
        """redefining the + operator for reverse order"""
        list_time1 = other[:]
        if self.len > len(other):
            i = len(other)
            while i < self.len:
                list_time1.append(0)
                i += 1
        list_time2 = NewList(list_time1)
        for j in range(self.len):
            list_time2.list[j] = list_time2.list[j] - self.list[j]
        return list_time2

    __rsub__ = inverse_sub

    def __getitem__(self, key):
        """override get item"""
        return self.list[key]

    def sum_of_list(self, arr):
        """getting the sum of the elements of a list"""
        total = 0
        for i in range(len(arr)):
            total = total + arr[i]
        return total

    def __lt__(self, other):
        """overriding operator <"""
        return self.sum_of_list(self.list) < self.sum_of_list(other)

    def __eq__(self, other):
        """overriding operator =="""
        return self.sum_of_list(self.list) == self.sum_of_list(other)

    def __ne__(self, other):
        """overriding operator !="""
        return self.sum_of_list(self.list) != self.sum_of_list(other)

    def __gt__(self, other):
        """overriding operator >"""
        return self.sum_of_list(self.list) > self.sum_of_list(other)
