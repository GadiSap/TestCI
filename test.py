import unittest
from main import img_proc
class EasyTest (unittest.TestCase):
    def test_mean0 (self):
        [ave, sd] = img_proc("test_image0.csv")
        self.assertEqual(ave, 0)

    def test_mean70 (self):
        [ave, sd] = img_proc("test_image70.csv")
        self.assertEqual(ave, 70)
        self.assertEqual(sd, 0)


if __name__ == '__main__':
    unittest.main()
