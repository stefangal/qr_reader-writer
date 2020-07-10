from main import Read
import unittest


class TestRead(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.rd = Read()

    def test_read_QR_code(self):
        txt = "hello world"
        path = r"C:\Users\stefan.gal\Documents\Python\GithubForks\qr_reader-writer\tests"
        x = self.rd.read_QR_code(path)
        print(x)
        self.assertEqual("http://en.m.wikipedia.org", x, "Not the same qr code")

if __name__ == "__main__":
    unittest.main()