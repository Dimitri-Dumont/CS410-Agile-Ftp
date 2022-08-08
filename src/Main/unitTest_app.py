from re import A
import unittest
from unittest.mock import patch
import app
import io
import sys
import os
from ftplib import FTP


class TestStringMethods(unittest.TestCase):

    def testConnection(self):
        info = {
            "host": '66.220.9.50',
            "user": 'DimitriDumont',
            "pw": 'Pergina93.'
        }
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        app.connect(info)
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(),
                         'Connected to ' + info["host"]+'\n')

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

        info = {
            "host": '66.220.9.50',
            "user": 'DimitriDumont',
            "pw": 'Pergina93.'
        }

        ftps = app.connect(info)
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
        sys.stdin = io.StringIO('newFolder')
        app.listDirLocal()
        self.assertIn('Files and directories in ', capturedOutput.getvalue()
                      )

    def testGetFileFromServer(self):
        # For this test to work you need to have a folder
        # called My Documents in your server with a file called
        # SampleText.txt

        info = {
            "host": '66.220.9.50',
            "user": 'DimitriDumont',
            "pw": 'Pergina93.'
        }
        ftps = app.connect(info)
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

    # def testRenameServer(self):
    #     ftp = FTP()
    #     myPath = ftp.cwd
    #     fileName = "testFile.txt"
    #     newName = "mytestFile.txt"
    #     ftp.rename(fileName, newName)
    #     check = ftp.myPath.exists('mytestFile.txt')
    #     self.assertTrue(check)

    @patch('app.createDirectory', return_value=b'newFolder5')
    def testCreateDirectoryServer(self, mock_createDirectory):
        # For this test to work you need to have a folder
        # called agileclass2 on your server

        # info = {
        #     "host": '66.220.9.50',
        #     "user": 'agileclass3',
        #     "pw": 'agile123!'
        # }
        # ftps = app.connect(info)
        # sys.stdin = io.StringIO('My Documents')
        # sys.stdin = io.StringIO('newDirectory')
        # app.createDirectory(ftps)
        # path = ftps.cwd
        # check = ftps.path.exists('agileclass2/newFolder4')

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


if __name__ == '__main__':
    unittest.main()
