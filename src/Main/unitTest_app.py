from re import A, T
import unittest
from unittest.mock import patch
import app
import io
import sys
import os
from ftplib import FTP


class TestStringMethods(unittest.TestCase):
    info = {
                "host": '66.220.9.50',
                "user": 'agile_class',
                "pw": 'password123!'
            }
    def testConnection(self):
        
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app.connect(self.info)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         'Connected to ' + self.info["host"]+'\n')

    def testDisconnectServer(self):
        ftps = FTP()
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        ftp = app.disconnect(ftps)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         'Disconnection Successful' + '\n')

    def testDirectoriesFilesServer(self):
        # This is connecting to my local host file server.
        # you would need to change it to your local host or
        # webserver for this to run

        ftps = app.connect(self.info)
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app.listDir(ftps)
        sys.stdout = sys.__stdout__
        self.assertIn("List of directories and files on server", capturedOutput.getvalue()
                      )
        ftps.close()

    def testDirectoriesFilesLocal(self):

        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        sys.stdin = io.StringIO('/')
        app.listDirLocal()
        self.assertIn('Files and directories in ', capturedOutput.getvalue()
                      )

    def testGetFileFromServer(self):
        # For this test to work you need to have a folder
        # called My Documents in your server with a file called
        # SampleText.txt

        ftps = app.connect(self.info)
        app.getFile(ftps)

        path = os.getcwd()
        check = os.path.exists('SampleText.txt')
        self.assertTrue(check)
        ftps.close()

    @patch('app.localRename', return_value=b'mytestFile.txt')
    def testRenameLocal(self, mock_localRename):

        mock_localRename.return_value = 'testFile.txt'
        mock_localRename.return_value = 'mytestFile.txt'
        self.assertEqual(app.localRename(), "mytestFile.txt")

    def testRenameServer(self):
        ftp = app.connect(self.info)
        try:
            app.remoteRename(ftp,"/","DONOTDELETE.txt","testRenamed.txt")
               
        except:
            self.fail("Exception thrown"); # assert error not thrown
        app.remoteRename(ftp,"/","testRenamed.txt","DONOTDELETE.txt") # reset file name to original

    def testCopyDir(self):
        ftp = app.connect(self.info)
        try:
            app.copyDirHelp(ftp,os.getcwd() + "/testDir")
        except:
            self.fail("Exception thrown"); # assert error not thrown

    def testGetMult(self):
            ftp = app.connect(self.info)
            try:
                app.getMultiple(ftp,"/testDir", os.getcwd())
            except:
                self.fail("Exception thrown"); # assert error not thrown

    @patch('app.createDirectory', return_value=b'newFolder5')
    def testCreateDirectoryServer(self, mock_createDirectory):

        mock_createDirectory.return_value = 'agileclass2'
        mock_createDirectory.return_value = 'newFolder5'

        self.assertTrue(app.createDirectory, "newFolder5")

    @patch('app.deleteDirectory')
    def testDeleteDirectoryServer(self, mockdeleteDirectory):
        mockdeleteDirectory.return_value = 'parentFolder'
        mockdeleteDirectory.return_value = 'childFolder'

        self.assertTrue(app.deleteDirectory, "newFolder5")

    @patch('app.deleteFile', return_value=b'')
    def testDeleteFileServer(self, mockDeleteFile):
        mockDeleteFile.return_value = 'parentFolder'
        mockDeleteFile.return_value = 'sampletext.txt'

        self.assertTrue(app.deleteDirectory, " ")

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
        self.assertEqual(capturedOutput.getvalue(),'Connected to ' + info["host"]+ '\n')


if __name__ == '__main__':
    unittest.main()
