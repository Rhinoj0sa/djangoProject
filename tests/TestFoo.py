import unittest


class TestFoo(unittest.TestCase):
    def test_foo(self):
        self.assertEqual(1, 1)


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, 1)  # add assertion here


if __name__ == '__main__':
    unittest.main()
