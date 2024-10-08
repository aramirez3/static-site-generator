import unittest

class AssertionHelper(unittest.TestCase):
    def assert_exception_and_message(self, func, exception_object, expected_message):
        with self.assertRaises(exception_object) as cm:
            func()
        self.assertEqual(str(cm.exception), expected_message)