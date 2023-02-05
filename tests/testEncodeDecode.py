import os
import sys
import unittest

sys.path.append('../hips-hack')
from src.hips_hack.stenography import decode, encode


class TestEncodingDecoding(unittest.TestCase):

    def test_encoding_decoding(self):
        encode('tests/stockimage.png','test','tests/stockimage_encoded.png')
        self.assertEqual(decode('tests/stockimage_encoded.png'), 'test')
    
    def test_long_encoding_decoding(self):
        input_data = 'lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out\
                                            lets see if this works and if it does then we can use this to encode a lot of data into \
            an image and maybe give it a try with a video and see if that works too becasue that would be really \
                cool and i would like to see if it works and lets give it a very long string to just test things\
                     out maybe i can write a whole paragraph and itll stilllllllllll work but lets test this out \
                        im going to double this and test it, lets see if this works and if it does then we can use \
                            this to encode a lot of data into an image and maybe give it a try with a video and \
                                see if that works too becasue that would be really cool and i would like to see \
                                    if it works and lets give it a very long string to just test things out maybe \
                                        i can write a whole paragraph and itll stilllllllllll work but lets test this out'

        encode('tests/stockimage.png',input_data,'tests/stockimage_encoded.png')
        decodedText = decode('tests/stockimage_encoded.png')
        self.assertEqual(decodedText, input_data)


unittest.main()
