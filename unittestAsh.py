import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test_HMAC(self):
        self.assertEqual(True, False)
    def test_IV(self):
        self.assertEqual(True, False)
    def test_Salt(self):
        self.assertEqual(True, False)
    def test_Pepper(self):
        self.assertEqual(True, False)
    def test_Iterations(self):
        self.assertEqual(True, False)
    def test_EncOutputBytes(self):
        self.assertEqual(True, False)
    def test_EncOutputString(self):
        self.assertEqual(True, False)

    '''DECRYPTION TESTING'''
    def test_RecHMAC(self):
        self.assertEqual(True, False)
    def test_RecIV(self):
        self.assertEqual(True, False)
    def test_RecSalt(self):
        self.assertEqual(True, False)
    def test_RecPepper(self):
        self.assertEqual(True, False)
    def test_RecIterations(self):
        self.assertEqual(True, False)
    def test_DecOutputBytes(self):
        self.assertEqual(True, False)
    def test_DecOutputString(self):
        self.assertEqual(True, False)



if __name__ == '__main__':
    unittest.main()
