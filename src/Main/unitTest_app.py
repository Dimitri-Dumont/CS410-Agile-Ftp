import unittest
import app
import io
import sys


class TestStringMethods(unittest.TestCase):

    def test_connection(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        host = 'localhost'
        user = 'Test'
        pw = 'RubberDuck'
        # ftp = app.connect(host,user,pw)
        # sys.stdout = sys.__stdout__                     # Capture stdout
        # self.assertEqual(capturedOutput.getvalue(),'Connected to ' + host +'\n')   # Assert console output is expected value.

    def test_ConnectionInfo_success(self):
        info = app.saveInfo()
        self.assertEqual(info["host"], "66.220.9.50")
        self.assertEqual(info["user"], "agile_class")
        self.assertEqual(info["pw"], "password123!")

    def test_UseConnInfo_success(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput

        info = app.saveInfo()
        ftp = app.connect(info)

        sys.stdout = sys.__stdout__
        # Assert console output is expected value.
        self.assertEqual(capturedOutput.getvalue(),
                         'Connected to ' + info["host"])


if __name__ == '__main__':
    unittest.main()
