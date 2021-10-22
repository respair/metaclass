from metaclass import MakeCustomMetaclass
import unittest


class MyTestCase(unittest.TestCase):

    def foo(self):
        return 10

    def setUp(self):
        """instantiating a class"""
        self.MyClass = MakeCustomMetaclass("MyClass", (object,), dict(item=100, foo=self.foo))

    def test_custom_dict_exist(self):
        try:
            self.assertFalse("custom___dict__" in self.MyClass.custom___dict__.keys())
        except AttributeError:
            pass

    def test_custom_dict(self):
        self.assertFalse("custom___dict__" in self.MyClass.__dict__.keys())

    def test_dict(self):
        self.assertTrue("__dict__" in self.MyClass.__dict__.keys())

    def test_custom_item_exist(self):
        self.assertTrue("custom_item" in self.MyClass.__dict__.keys())

    def test_custom_item(self):
        self.assertEqual(self.MyClass.custom_item, 100)

    def test_item(self):
        self.assertFalse("item" in self.MyClass.__dict__.keys())

    def test_custom_foo_exist(self):
        self.assertTrue("custom_foo" in self.MyClass.__dict__.keys())

    def test_custom_foo(self):
        self.assertEqual(self.MyClass.custom_foo(), 10)

    def test_foo(self):
        self.assertFalse("foo" in self.MyClass.__dict__.keys())

    def test_doc(self):
        self.assertEqual(self.MyClass.__doc__, None)

    def test_custom_doc(self):
        self.assertFalse("custom___doc__" in self.MyClass.__dict__.keys())
