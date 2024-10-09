import unittest

class AssertionHelper(unittest.TestCase):
    def assert_exception_and_message(self, func, exception_object, expected_message, param=None):
        with self.assertRaises(exception_object) as cm:
            if param is None:
                func()
            else:
                func(param)
        self.assertEqual(str(cm.exception), expected_message)