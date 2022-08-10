from ftplib import FTP
from ftplib import error_perm
import os
import sys
import signal


class FTPClient:
    def menu(self):
        print("1. Disconnect from ftp server (Exit)")
        print("2. List directories & files on server")
        print("3. List directories & files on local machine")
        print("4. Get a File From Server")
        print("5. Get Multiple Files From Server ")
        print("6. Create Directory On Server")
        print("7. Delete Directory From Server")
        print("8. Upload File On Server")
        print("9. Delete File From Server")
        print("10. Upload Multiple Files On Server")
        print("11. Copy directories")
        print("12. Rename File On Remote Server")
        print("13. Rename File On Local Machine")

        user_input = input("\nEnter number of what you would like to do:\n")
        return user_input


    def options(self,user_input, ftp):
        match user_input:
            case'1':
                self.disconnect(ftp)
            case'2':
                self.listDir(ftp)
            case'3':
                self.listDirLocal()
            case'4':
                self.getFile(ftp)
            case'5':
                self.getMultiple(ftp)
            case'6':
                self.createDirectory(ftp)
            case'7':
                self.deleteDirectory(ftp)
            case'8':
                self.uploadFile(ftp)
            case'9':
                self.deleteFile(ftp)
            case'10':
                self.uploadMultiple(ftp)
            case'11':
                self.copyDirHelp(ftp)
            case'12':
                self.remoteRename(ftp)
            case'13':
                self.localRename()


    def connect(self,info):
        try:
            ftp = FTP()
            ftp.connect(info["host"], 21)
            ftp.login(info["user"], info["pw"])
        except:
            print('Connection failed')
        else:
            print('Connected to ' + info["host"])
            return ftp


    def disconnect(self,ftp):
        try:
            ftp.close()
        except:
            print("Error occured closing connection")
        else:
            print("Disconnection Successful")


    def listDir(self, ftp):
        print("*"*50, "list", "*"*50)
        ftp.dir()
        # This line needs to be there for unit test 3 to work
        print("List of directories and files on server")


    def listDirLocal(self):  # Only listing directories at the moment not files
        print("Current directory: " + os.getcwd())
        path = input("Enter path you wish to view: ")
        dir_list = os.listdir(path)
        print("Files and directories in '", path, "' :")
        print(dir_list)


    def getFile(self, ftp):
        FILENAME = "SampleText.txt"
        ftp.cwd("My Documents")

        with open(FILENAME, 'wb') as fp:
            ftp.retrbinary('RETR ' + FILENAME, fp.write)


    def copyDirHelp(self, ftp):
        path = '\\'
        # example destination C:\temp\
        destination = input("destination direcotry?\n")
        copyDir(path, destination, ftp)

    # copyDir copies all directories (not files) to designated local destination


    def copyDir(self, path, destination, ftp):
        try:
            ftp.cwd(path)
            # clone path to destination
            os.chdir(destination)
            os.mkdir(destination[0:len(destination)-1]+path)
            print(destination[0:len(destination)-1]+path+" built")
        except OSError:
            # folder already exists at destination
            pass
        except error_perm:
            print("error: could not change to "+path)
            sys.exit()

        # list children:
        filelist = ftp.nlst()

        for file in filelist:
            try:
                # check if folder or file
                ftp.cwd(path+file+"/")
                # if file explore
                copyDir(path+file+"/", destination, ftp)
            except error_perm:
                # not a folder with accessible content
                return


    # gets multiple files from specified directory
    def getMultiple(self,ftp):
        current_directory = ftp.pwd()
        print("Current directory: " + current_directory)
        # enter directory of FTP
        ftp_directory = input(
            "Enter path of directory on FTP server (don't forget to include /): ")
        # goto that directory
        ftp.cwd(ftp_directory)
        # grab all the files in that directory
        files_list = ftp.nlst(ftp_directory)
        print("Current directory: " + os.getcwd())
        local_path = input("Enter desired path on your local machine: ")
        for file in files_list:
            print("local path: " + local_path)
            local_fn = os.path.join(local_path, os.path.basename(file))
            print(local_fn)
            print("Downloading " + file + " from remote server.")
            local_file = open(local_fn, "wb")
            ftp.retrbinary("RETR " + file, local_file.write)
            local_file.close()
            print()


    def createDirectory(self,ftp):
        path = input("Input path you wish to create a directory in: ")
        name = input("Input name of the directory: ")
        ftp.cwd(path)
        ftp.mkd(name)


    def deleteDirectory(self, ftp):
        self.listDir(ftp)
        path = input("Input path you wish to delete a directory in: ")
        ftp.cwd(path)
        current_directory = ftp.pwd()
        print("Currently working in: " + current_directory)
        directory = input("Enter name of directory you wish to delete: ")
        ftp.rmd(directory)


    def deleteFile(self, ftp):
        path = input("Input path of file you wish to delete: ")
        ftp.cwd(path)
        current_directory = ftp.pwd()
        print("Currently working in: " + current_directory)
        self.listDir(ftp)
        file = input("Enter name of the file you wish to delete: ")
        ftp.delete(file)


    def uploadFile(self, ftp):
        ftp.encoding = 'utf-8'
        path = input(
            "What path on the server do you want to upload this file to: ")
        ftp.cwd(path)
        current_directory = ftp.pwd()
        print("Currently working in: " + current_directory)
        filename = input("Enter local file name you wish to upload: ")
        with open(filename, 'rb') as file:
            ftp.storbinary(f'STOR {filename}', file)

    # uploads multiple files to server


    def uploadMultiple(self, sftp):
        sftp.encoding = 'utf8'

        filesToUpload = []
        file_number = 1
        user_input = ''

        print("\nEnter names of files to upload below. Press x when done/to exit.")

        while (user_input != 'x'):
            user_input = input("File name " + str(file_number) + ": ")
            if user_input != 'x':
                filesToUpload.append(user_input)
            file_number += 1

        i = 0
        while i < len(filesToUpload):
            with open(filesToUpload[i], 'rb') as fp:
                sftp.storbinary('STOR ' + filesToUpload[i], fp)
            i += 1

    # rename a file on the remote server


    def remoteRename(self,ftp):
        path = input("Input path of file you wish to rename: ")
        fromName = input("Input name of file you want to rename: ")
        toName = input("What would you like to rename it to: ")
        ftp.cwd(path)
        ftp.rename(fromName, toName)

    # rename a file on your local machine


    def localRename(self):
        currentPath = os.getcwd()
        print("Your current working directory: " + currentPath)
        oldFileName = input("Enter path/filename of file you wish to change: ")
        newFileName = input(
            "Enter path/filename of file you wish to change it to: ")
        os.rename(oldFileName, newFileName)


    def saveInfo(self):
        info = {
            "host": '66.220.9.50',
            "user": 'agile_class',
            "pw": 'password123!'
        }
        return info


    def timeout_handler(self, signal, frame):
        raise Exception(f'Disconnected due to inactivity')


    def main(self):
        info = self.saveInfo()
        ftp = self.connect(info)

        user_input = 0
        signal.alarm(300)  # times out after 5 minutes
        signal.signal(signal.SIGALRM, self.timeout_handler)

        try:
            while int(user_input) != 1:
                user_input = self.menu()
                self.options(user_input, ftp)
        except Exception as e:
            print(e)
            self.disconnect(ftp)


if __name__ == "__main__":
    client = FTPClient()
    client.main()
