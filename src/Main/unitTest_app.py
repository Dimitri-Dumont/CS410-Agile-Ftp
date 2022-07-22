import unittest
import app
import io
import sys

class TestStringMethods(unittest.TestCase):

    def test_connection(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput                     #  and redirect stdout.
        host = 'localhost'
        user = 'Test'
        pw = 'RubberDuck'
        ftp = app.connect(host,user,pw)                                    
        sys.stdout = sys.__stdout__                     # Capture stdout
        self.assertEqual(capturedOutput.getvalue(),'Connect to ' + host +'\n')   # Assert console output is expected value.
    

if __name__ == '__main__':
    unittest.main()