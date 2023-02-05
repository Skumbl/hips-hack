import unittest
from hips_hack.stenography import encode, decode
import os

class TestEncodingDecoding(unittest.TestCase):

    def test_encoding_decoding(self):
        encode('tests/stockimage.png','test','tests/stockimage_encoded.png')
        self.assertEqual(decode('tests/stockimage_encoded.png'), 'test')

unittest.main()