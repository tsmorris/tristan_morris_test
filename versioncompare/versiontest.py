import unittest
import versioncompare as VC

class TestVersionComparison(unittest.TestCase):
    def test_greater(self):
        self.assertEqual(VC.compare_versions("1.4", "1.3"), 1)

    def test_lesser(self):
        self.assertEqual(VC.compare_versions("1.3", "1.4"), -1)

    def test_equal(self):
        self.assertEqual(VC.compare_versions("1.4", "1.4"), 0)

    def test_incomparable(self):
        self.assertEqual(VC.compare_versions("1.1.1.1.1.1.1.1.1", "1"), 0)

    def test_input(self):
        with self.assertRaises(TypeError):
            VC.compare_versions(1.23, "1.1.1")

    def test_long(self):
        A = "1"
        for x in range(1000):
            A = A+".100"
        B = A+".0"
        A = A+".1"
        self.assertEqual(VC.compare_versions(A, B), 1)
