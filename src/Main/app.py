from ftplib import FTP
<<<<<<< HEAD
from sys import platform
import os

=======
from ftplib import error_perm
import os
import sys
>>>>>>> 336b9b1e9574213bc89f88d3494e70b2dd439f69

def menu():
    print("1. Disconnect from ftp server (Exit)")
    print("2. List directories & files on server")
    print("3. List directories & files on local machine")
<<<<<<< HEAD
    print("4. Make Directory in remote server")
    print("5. Delete file from remote server ")
    print("6. Get file from remote server")
    print("7. List directories and files on remote server")
    print("8. Get multiple files")
    print("9. Delete file from remote server ")
=======
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
>>>>>>> 336b9b1e9574213bc89f88d3494e70b2dd439f69

    user_input = input("\nEnter number of what you would like to do:\n")
    return user_input

<<<<<<< HEAD

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

=======
def options(user_input, ftp):
    match user_input:
        case'1':
            disconnect(ftp)
        case'2':
            listDir(ftp)
        case'3':
            listDirLocal()
        case'4':
            getFile(ftp)
        case'5':
            getMultiple(ftp)
        case'6':
            createDirectory(ftp)
        case'7':
            deleteDirectory(ftp)
        case'8':
            uploadFile(ftp)
        case'9':
            deleteFile(ftp)
        case'10':
            uploadMultiple(ftp)
        case'11':
            copyDirHelp(ftp)
        case'12':
            remoteRename(ftp)
        case'13':
            localRename()
>>>>>>> 336b9b1e9574213bc89f88d3494e70b2dd439f69

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

<<<<<<< HEAD

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


=======
def disconnect(ftp):
    try:
        ftp.close()
    except:
        print("Error occured closing connection")
    else:
        print("Disconnection Successful")

def listDir(ftp):
    print("*"*50,"list","*"*50)
    ftp.dir()
    
def listDirLocal(): # Only listing directories at the moment not files
    print("Current directory: " + os.getcwd())
    path = input("Enter path you wish to view: ")
    dir_list =os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)

def getFile(ftp):
    FILENAME = "SampleText.txt"
    ftp.cwd("My Documents")
   


    with open(FILENAME, 'wb') as fp:
        ftp.retrbinary('RETR ' + FILENAME, fp.write)

def copyDirHelp(ftp):
    path = '\\'
    # example destination C:\temp\
    destination = input("destination direcotry?\n")
    copyDir(path,destination,ftp)

# copyDir copies all directories (not files) to designated local destination
def copyDir(path,destination,ftp):
    try:
        ftp.cwd(path)
        #clone path to destination
        os.chdir(destination)
        os.mkdir(destination[0:len(destination)-1]+path)
        print (destination[0:len(destination)-1]+path+" built")
    except OSError:
        #folder already exists at destination
        pass
    except error_perm:
        print ( "error: could not change to "+path )
        sys.exit()

    #list children:
    filelist=ftp.nlst()
    
    for file in filelist:
        try:
            #check if folder or file
            ftp.cwd(path+file+"/")
            #if file explore
            copyDir(path+file+"/",destination,ftp)
        except error_perm:
            #not a folder with accessible content
            return


#gets multiple files from specified directory
def getMultiple(ftp):
    current_directory = ftp.pwd()
    print("Current directory: " + current_directory)
    #enter directory of FTP
    ftp_directory = input("Enter path of directory on FTP server (don't forget to include /): ")
    #goto that directory
    ftp.cwd(ftp_directory)
    #grab all the files in that directory
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

def createDirectory(ftp):
    path = input("Input path you wish to create a directory in: ")
    name = input("Input name of the directory: ")
    ftp.cwd(path)
    ftp.mkd(name)


def deleteDirectory(ftp):
    listDir(ftp)
    path = input("Input path you wish to delete a directory in: ")
    ftp.cwd(path)
    current_directory = ftp.pwd()
    print("Currently working in: " + current_directory)
    directory = input("Enter name of directory you wish to delete: ")
    ftp.rmd(directory)

def deleteFile(ftp):
    path = input("Input path of file you wish to delete: ")
    ftp.cwd(path)
    current_directory = ftp.pwd()
    print("Currently working in: " + current_directory)
    listDir(ftp)
    file= input("Enter name of the file you wish to delete: ")
    ftp.delete(file)

def uploadFile(ftp):
    ftp.encoding = 'utf-8'
    path = input("What path on the server do you want to upload this file to: ")
    ftp.cwd(path)
    current_directory = ftp.pwd()
    print("Currently working in: " + current_directory)
    filename= input("Enter local file name you wish to upload: ")
    with open(filename, 'rb') as file:
        ftp.storbinary(f'STOR {filename}', file) 

#uploads multiple files to server
def uploadMultiple(sftp):
    sftp.encoding = 'utf8'

    filesToUpload = []
    file_number = 1
    user_input = ''

    print("\nEnter names of files to upload below. Press x when done/to exit.")

    while (user_input!= 'x'):
        user_input = input("File name " + str(file_number) + ": ")
        if user_input != 'x':
            filesToUpload.append(user_input)
        file_number += 1

    i = 0
    while i < len(filesToUpload):
        with open(filesToUpload[i], 'rb') as fp:
            sftp.storbinary('STOR ' + filesToUpload[i], fp)
        i += 1

#rename a file on the remote server
def remoteRename(ftp):
    path = input("Input path of file you wish to rename: ")
    fromName = input("Input name of file you want to rename: ")
    toName = input("What would you like to rename it to: ")
    ftp.cwd(path)
    ftp.rename(fromName,toName)

#rename a file on your local machine
def localRename():
    currentPath = os.getcwd()
    print("Your current working directory: " + currentPath)
    oldFileName = input("Enter path/filename of file you wish to change: ")
    newFileName = input("Enter path/filename of file you wish to change it to: ")
    os.rename(oldFileName,newFileName)


def main():
    host = '66.220.9.50'
    user = 'agile_class'
    pw = 'password123!'
    ftp = connect(host,user,pw)
    user_input = 0
    while int(user_input) != 1:
        user_input = menu()
        options(user_input,ftp)

>>>>>>> 336b9b1e9574213bc89f88d3494e70b2dd439f69
if __name__ == "__main__":
    main()
