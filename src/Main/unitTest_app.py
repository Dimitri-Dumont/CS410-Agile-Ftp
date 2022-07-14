import unittest
from app import main
import io
import sys

class TestStringMethods(unittest.TestCase):

    def test_main(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        main()                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(),"Hola\n")   # Assert console output is expected value.
    

if __name__ == '__main__':
    unittest.main()