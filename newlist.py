class NewList(list):

    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.list = arr
        self.len = len(arr)

    def append(self, item):
        self.list.append(item)
        self.len = len(self.list)

    def copy(self, arr):
        self.list = []
        for i in range(len(arr)):
            self.list.append(arr[i])
        self.len = len(self.list)

    def new_size_list(self, other):
        list_time = self.list[:]
        if self.len < len(other):
            i = self.len
            while i < len(other):
                list_time.append(0)
                i += 1
        return NewList(list_time)

    def __len__(self):
        return self.len

    def __add__(self, other):
        list_time = self.new_size_list(other)
        for j in range(len(other)):
            list_time.list[j] = list_time.list[j] + other[j]
        return list_time

    __radd__ = __add__

    def __sub__(self, other):
        list_time = self.new_size_list(other)
        for j in range(len(other)):
            list_time.list[j] = list_time.list[j] - other[j]
        return list_time

    def inverse_sub(self, other):
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
        return self.list[key]

    def sum_of_list(self, arr):
        total = 0
        for i in range(len(arr)):
            total = total + arr[i]
        return total

    def __lt__(self, other):
        return self.sum_of_list(self.list) < self.sum_of_list(other)

    def __eq__(self, other):
        return self.sum_of_list(self.list) == self.sum_of_list(other)

    def __ne__(self, other):
        return self.sum_of_list(self.list) != self.sum_of_list(other)

    def __gt__(self, other):
        return self.sum_of_list(self.list) > self.sum_of_list(other)
