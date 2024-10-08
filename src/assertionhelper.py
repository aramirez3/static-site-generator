import unittest

class AssertionHelper(unittest.TestCase):
    def assert_exception_and_message(self, func, exception_object, expected_message, node=None):
        with self.assertRaises(exception_object) as cm:
            if node is None:
                func()
            else:
                func(node)
        self.assertEqual(str(cm.exception), expected_message)