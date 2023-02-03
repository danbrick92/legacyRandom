import unittest


class ArrayList:
    def __init__(self, size=10):
        if size < 1:
            raise Exception("Size must be at least 1")
        self.size = size
        self.last = 0
        self.the_list = [None] * self.size

    def check_index_valid(self, index):
        return index <= self.last

    def __check_need_expand_list(self):
        if self.the_list[-1] is not None:
            return True
        return False

    def __expand(self):
        self.size *= 2
        new_list = [None] * self.size
        for i in range(len(self.the_list)):
            new_list[i] = self.the_list[i]
        self.the_list = new_list

    def insert(self, value, index=None):
        if index is None:
            index = self.last

        if self.__check_need_expand_list():
            self.__expand()

        if self.check_index_valid(index) is False:
            return False

        prev = value
        for i in range(index, self.last+1):
            new = prev
            prev = self.the_list[i]
            self.the_list[i] = new
            if prev is None:
                break

        self.last += 1
        return True

    def remove(self, index=None):
        if index is None:
            index = self.last-1

        if self.check_index_valid(index) is False:
            return False

        prev = None
        for i in range(self.last-1, index-1, -1):
            new = prev
            prev = self.the_list[i]
            self.the_list[i] = new

        self.last -= 1
        return True

    def get_value_by_index(self, index):
        if self.check_index_valid(index) is False:
            return False

        return self.the_list[index]

    def get_index_by_value(self, value):
        for i in range(len(self.the_list)):
            if self.the_list[i] == value:
                return i
        return False

    def update_by_index(self, index, value):
        if self.check_index_valid(index) is False:
            return False

        self.the_list[index] = value
        return True


class TestArrayList(unittest.TestCase):

    def test_basic_insert(self):
        a = ArrayList()
        a.insert("dan")
        assert a.get_index_by_value('dan') == 0
        assert a.get_value_by_index(0) == 'dan'

    def test_basic_remove(self):
        a = ArrayList(size=1)
        a.insert("dan")
        a.remove(0)
        assert a.the_list == [None]

    def test_basic_get(self):
        a = ArrayList()
        a.insert("dan")
        a.insert("bob")
        a.insert("tim")
        assert a.get_index_by_value('bob') == 1
        assert a.get_value_by_index(2) == 'tim'

    def test_update(self):
        a = ArrayList(size=2)
        a.insert('dan')
        a.insert('bob')
        a.update_by_index(0, 'tim')
        assert a.the_list == ['tim', 'bob']

    def test_expand(self):
        a = ArrayList(size=1)
        a.insert('dan')
        a.insert('bob')
        a.insert('tim')
        assert a.the_list == ['dan', 'bob', 'tim', None]

    def test_fail_array_size(self):
        success = False
        try:
            a = ArrayList(size=0)
        except Exception as e:
            success = True
        assert success

    def test_fail_out_bound_index(self):
        a = ArrayList(size=2)
        a.insert('dan')
        a.insert('bob')
        assert a.get_value_by_index(3) is False

    def test_fail_get_by_value(self):
        a = ArrayList()
        a.insert('dan')
        a.insert('bob')
        assert a.get_index_by_value('tim') is False
