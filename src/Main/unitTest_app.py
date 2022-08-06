import unittest
import app
import io
import sys
import os
from ftplib import FTP


class TestStringMethods(unittest.TestCase):

    def testConnection(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        host = '66.220.9.50'
        user = 'agile_class'
        pw = 'password123!'
        ftp = app.connect(host, user, pw)
        sys.stdout = sys.__stdout__                     # Capture stdout
        # Assert console output is expected value.
        self.assertEqual(capturedOutput.getvalue(),
                         'Connected to ' + host + '\n')

    def testDisconnectServer(self):
        ftps = FTP()

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        ftp = app.disconnect(ftps)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         'Disconnection Successful' + '\n')

    def testDirectoriesFilesServer(self):
        ftps = FTP()

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        ftp = app.listDir(ftps)
        sys.stdout = sys.__stdout__
        self.assertAlmostEquals(capturedOutput.getvalue(),
                                'List of directories and files on server' + '\n')

    def testDirectoriesFilesLocal(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        path = "newFolder"
        ftp = app.listDirLocal()
        dir_list = os.listdir(path)
        sys.stdout = sys.__stdout__
        self.assertAlmostEquals(capturedOutput.getvalue(),
                                'Files and directories in ' + path + ' :')

    def testGetFileFromServer(self):
        ftp = FTP()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        FILENAME = "testFile.txt"
        ftp.cwd("My Documents")
        with open(FILENAME, 'wb') as fp:
            ftp.retrbinary('RETR ' + FILENAME, fp.write)
        myPath = os.getcwd()
        check = os.myPath.exists('testFile.txt')
        self.assertTrue(check)

    def testRenameLocal(self):
        myPath = os.getcwd()
        fileName = "testFile.txt"
        newName = "mytestFile.txt"
        os.rename(fileName, newName)
        check = os.myPath.exists('mytestFile.txt')
        self.assertTrue(check)

    def testRenameServer(self):
        ftp = FTP()
        myPath = ftp.cwd
        fileName = "testFile.txt"
        newName = "mytestFile.txt"
        ftp.rename(fileName, newName)
        check = ftp.myPath.exists('mytestFile.txt')
        self.assertTrue(check)

    def testCreateDirectoryServer(self):
        ftp = FTP()

        myPath = ftp.cwd
        directoryName = "newDirectory"
        ftp.mkd(directoryName)
        check = ftp.myPath.exists('newDirectory')
        self.assertTrue(check)

    def testDeleteDirectoryServer(self):
        ftp = FTP()
        myPath = ftp.cwd
        directoryName = "newDirectory"
        ftp.rmd(directoryName)
        check = ftp.myPath.exists('newDirectory')
        self.assertFalse(check)

    def testDeleteFileServer(self):
        ftp = FTP()
        myPath = ftp.cwd
        fileName = "testFile.txt"
        ftp.delete(fileName)
        check = ftp.myPath.exists('testFile.txt')
        self.assertFalse(check)


if __name__ == '__main__':
    unittest.main()
