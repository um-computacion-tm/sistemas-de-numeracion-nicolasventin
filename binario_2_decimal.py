import unittest 


class Test_Numeracion(unittest.TestCase):
    def test_binario2decimal(self):
        self.assertEqual(binario2decimal, '01011100', 96)

if __name__ == '__main__':
    unittest.main()