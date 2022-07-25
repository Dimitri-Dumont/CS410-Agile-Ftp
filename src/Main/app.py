from ftplib import FTP
from sys import platform
import os


def menu():
    print("1. Disconnect from SFTP server")
    print("2. List directories & files on server")
    print("3. List directories & files on local machine")
    print("4. Make Directory in remote server")
    print("5. Delete file from remote server ")
    print("6. Get file from remote server")
    print("7. List directories and files on remote server")
    print("8. Get multiple files")
    print("9. Delete file from remote server ")

    user_input = input("Enter number of what you would like to do:\n")
    return user_input


def options(user_input, sftp):
    match user_input:
        case '1':
            disconnect(sftp)
        case '2':
            listDir(sftp)
        case '3':
            listFileDirLocal()
        case '4':
            createDirRemote(sftp)
        case '5':
            deleteFileRemote(sftp)


def connect(host, user, pw):
    try:
        ftp = FTP()
        ftp.connect(host, 21)
        ftp.login(user, pw)
    except:
        print('Connection failed')
    else:
        print('Connected to ' + host)
        return ftp


def disconnect(sftp):
    try:
        sftp.close()
    except:
        print("Error occured closing connection")
    else:
        print("Disconnected")


def listDir(sftp):
    sftp.dir()


def listDirLocal():  # Only listing directories at the moment not files

    with os.scandir('C:\\') as it:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)

    # If we don't use 'C:\\' and only go with os.scandir it will print the content of
    # folder for current directory. This way the function will be compatible with linux
    # and mac systems as well.


def listFileDirLocal():  # Listing files and directories + OS compatible

    with os.scandir() as it:
        for entry in it:
            if entry.is_dir() or entry.is_file() and not entry.name.startswith('.'):
                print(entry.name)


def createDirRemote(sftp):
    Choice = input(
        "Would you like to create file in current director or in a different directory")
    print("Press 1 for current directory ")
    print("Press 2 for a different directory ")

    if (Choice == 2):
        newPath = input(
            "Enter path of folder where you would like to create the directory")
        sftp.cwd(newPath)

    elif (Choice > 2 or Choice < 1):
        print("Invalid option. Either press 1 or 2")

    directoryName = input(
        "Enter name of directory that you would like to create")
    sftp.mkd(directoryName)


def createDirRemote(sftp):
    Choice = int(input(
        "Would you like to create file in current director or in a different directory \n Press 1 for current directory  \n Press 2 for a different directory \n"))

    if (Choice == 2):
        newPath = input(
            "Enter path of folder where you would like to create the directory \n")

        if not os.path.exists(newPath):
            raise IOError("Path doesn't exist")
            return
        else:
            sftp.cwd(newPath)

    elif (Choice > 2 or Choice < 1):
        print("Invalid option. Input can be either 1 or 2 \n")
        return

    directoryName = input(
        "Enter name of directory that you would like to create \n")

    sftp.mkd(directoryName)


def deleteFileRemote(sftp):
    Choice = int(input(
        "Would you like to delete a file from current directory or a different directory \n Press 1 for current directory \n Press 2 for a different directory "))

    if (Choice == 2):
        newPath = input(
            "Enter path of folder where you would like to delete the file \n")
        if not os.path.exists(directoryName):
            raise IOError("Path doesn't exist")
            return
        else:
            sftp.cwd(newPath)

    elif (Choice > 2 or Choice < 1):
        print("Invalid option selected")
        return

    directoryName = input(
        "Enter complete file name along with extension to delete ")
    sftp.delete(directoryName)


def main():
    # public ip once server is running remotley:
    #host = '67.160.144.238'

    print("Defaulting to local server for testing")
    host = '67.160.144.238'
    user = 'Test'
    pw = 'RubberDuck'
    ftp = connect(host, user, pw)
    user_input = menu()
    options(user_input, ftp)


if __name__ == "__main__":
    main()
