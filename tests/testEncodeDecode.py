import unittest
from hips_hack.stenography import encode, decode

class TestEncodingDecoding(unittest.TestCase):

    def test_multiply_by_three(self):
        encode('stockimage.png','test','stockimage_encoded.png')
        self.assertEqual(decode('stockimage_encoded.png'), 'test')
		# self.assertEqual(multiply_by_three(3), 9)

unittest.main()