from newlist import NewList
import unittest


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.list = NewList()
        self.array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

    def create_new_list(self, arr=None):
        if arr is None:
            arr = self.array
        self.list.copy(arr)
        return self.list

    def test_init_empty(self):
        self.assertEqual(self.list.list, [])

    def test_init_not_empty(self):
        test_list = NewList([1, 2, 3, 10, 15])
        self.assertEqual(test_list.list, [1, 2, 3, 10, 15])

    def test_append(self):
        for i in range(10):
            self.list.append(i)
        self.assertEqual(self.list.list, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_copy(self):
        self.list = self.create_new_list()
        self.assertEqual(self.list.list, self.array)

    def test_sum_of_list(self):
        self.list = self.create_new_list()
        total = self.list.sum_of_list(self.list)
        self.assertEqual(total, 66)

    def test_new_size_list(self):
        test_list = [0, 1, 2, 3, 4, 5]
        self.list.copy(test_list)
        test_list_new = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9]
        result_list = self.list.new_size_list(test_list_new)
        result_test_list = NewList([0, 1, 2, 3, 4, 5, 0, 0, 0, 0])
        self.assertEqual(result_list, result_test_list)

    def test_len_zero(self):
        self.assertEqual(len(self.list), 0)

    def test_len(self):
        self.list = self.create_new_list()
        self.assertEqual(len(self.list), 12)

    def test_empty_add_array(self):
        self.assertEqual((self.list + self.array).list, self.array)

    def test_new_list_add_array(self):
        self.list = self.create_new_list()
        list_add = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result_list = [10, 2, 10, 6, 0, 5, 0, 14, 16, 18, 10, 11, 100]
        self.assertEqual((self.list + list_add).list, result_list)

    def test_array_add_new_list(self):
        self.list = self.create_new_list()
        list_add = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result_list = [10, 2, 10, 6, 0, 5, 0, 14, 16, 18, 10, 11, 100]
        self.assertEqual((list_add + self.list).list, result_list)

    def test_immutable_add(self):
        self.list = self.create_new_list()
        list_add = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result = self.list + list_add
        self.assertEqual(self.list.list, self.array)

    def test_empty_sub_array(self):
        test_result = [-self.array[i] for i in range(len(self.array))]
        self.assertEqual((self.list - self.array).list, test_result)

    def test_new_list_sub_array(self):
        self.list = self.create_new_list()
        list_sub = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result_list = [-10, 0, -6, 0, 8, 5, 12, 0, 0, 0, 10, 11, -100]
        self.assertEqual((self.list - list_sub).list, result_list)

    def test_array_sub_new_list(self):
        self.list = self.create_new_list()
        list_sub = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result_list = [10, 0, 6, 0, -8, -5, -12, 0, 0, 0, -10, -11, 100]
        self.assertEqual((list_sub - self.list).list, result_list)

    def test_immutable_sub(self):
        self.list = self.create_new_list()
        list_sub = [10, 1, 8, 3, -4, 0, -6, 7, 8, 9, 0, 0, 100]
        result = self.list - list_sub
        self.assertEqual(self.list.list, self.array)

    def test_get(self):
        self.list = self.create_new_list()
        for i in range(10):
            self.assertEqual(self.list[i], i)

    def test_equal(self):
        self.list = self.create_new_list()
        test_list_new = NewList([33, 32, 1])
        self.assertTrue(test_list_new == self.list)

    def test_not_equal(self):
        self.list = self.create_new_list()
        test_list_new = NewList([33, 30, 1])
        self.assertTrue(test_list_new != self.list)

    def test_ge(self):
        self.list = self.create_new_list()
        test_list_new = NewList([33, 30, 1])
        self.assertTrue(self.list > test_list_new)

    def test_lt(self):
        self.list = self.create_new_list()
        test_list_new = NewList([33, 30, 1, 9])
        self.assertTrue(self.list < test_list_new)


