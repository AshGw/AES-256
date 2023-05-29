import unittest
import Ash
class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.message1 = 'Hello there testing if it works'
        self.message2 = b'Hello this is bytes now'
        self.mainkey = 'c3066e464350e68a144d6be3e35c879eac1b9f360139443ee3d9e1960725d6a4d3379af0a35b6a07d083ecc29c4ba03767ad6d48b8e9c20d319dd459da52a91a'
        self.ins1 = Ash.Enc(message=self.message1, mainkey=self.mainkey)
        self.string_message = self.ins1.encToStr()
        self.bytes_message = self.ins1.encToBytes()
        self.ins2 = Ash.Dec(message=self.bytes_message,mainkey=self.mainkey)
    def tearDown(self) -> None:
        pass
    def test_KeyLength(self):
        self.assertEqual(64, bytes.fromhex(Ash.Enc.genMainkey()).__len__())
    def test_KeyType(self):
        self.assertIs(str,type(Ash.Enc.genMainkey()))
    def test_HMAC(self):
        self.assertTrue(self.bytes_message[:64] == self.ins1.HMAC())
    def test_IV(self):
        self.assertTrue(self.bytes_message[64:80] == self.ins1.iv)
    def test_Salt(self):
        self.assertTrue(self.bytes_message[80:96] == self.ins1.salt)
    def test_Pepper(self):
        self.assertTrue(self.bytes_message[96:112] == self.ins1.pepper)
    def test_Iterations(self):
        self.assertTrue(self.bytes_message[112:116] == self.ins1.setupIterations())
    def test_Ciphertext(self):
        self.assertTrue(self.bytes_message[116:] == self.ins1.ciphertext())
    def test_TypeIterations(self):
        self.assertIs(bytes,type(self.ins1.setupIterations()))
    def test_IterationsFixed_size(self):
        self.assertEqual(4,self.ins1.setupIterations().__len__())

    # def test_OutOfRangeError(self):
    #     self.assertRaises(Ash.IterationsOutofaRangeErrorE,self.ins1.iterations < 50)
    def test_EncOutputBytes(self):
        self.assertIs(bytes,type(self.ins1.encToBytes()))
    def test_EncOutputString(self):
        self.assertIs(str,type(self.ins1.encToStr()))

    '''DECRYPTION TESTING'''

    # def test_RecHMAC(self):
    #     self.assertEqual(True, False)

    # def test_RecIV(self):
    #     self.assertEqual(True, False)

    # def test_RecSalt(self):
    #     self.assertEqual(True, False)

    # def test_RecPepper(self):
    #     self.assertEqual(True, False)

    # def test_RecIterations(self):
    #     self.assertEqual(True, False)

    # def test_DecOutputBytes(self):
    #     self.assertEqual(True, False)

    # def test_DecOutputString(self):
    #     self.assertEqual(True, False)




if __name__ == '__main__':
    unittest.main()
