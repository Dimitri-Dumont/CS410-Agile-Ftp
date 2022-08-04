from ftplib import FTP
import os

def menu():
    print("\n1. Disconnect from SFTP server (Exit)")
    print("2. List directories & files on server")
    print("3. List directories & files on local machine")
    print("4. Get file from remote server")
    print("5. List directories and files on remote server")
    print("6. Get multiple files")
    print("7. Delete file from remote server ")

    user_input = input("\nEnter number of what you would like to do:\n")
    return user_input

def options(user_input, sftp):
     match user_input:
        case '1':
            disconnect(sftp)
        case '2':
            listDir(sftp)
        case '3':
            listDirLocal()
        case '4':
            getFile(sftp)


def connect(host, user,pw):
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

def listDirLocal(): # Only listing directories at the moment not files
    with os.scandir('C:\\') as it:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)

# downloads a single file from server to local machine
def getFile(sftp):
    FILENAME = "SampleText.txt"
    sftp.cwd("My Documents")
    # print(sftp.pwd())
    # print(sftp.dir())


    with open(FILENAME, 'wb') as fp:
        sftp.retrbinary('RETR ' + FILENAME, fp.write)

#uploads multiple files to server
def putMultiple(sftp):
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

def main():
    host = '66.220.9.50'
    user = 'agile_class'
    pw = 'password123!'
    ftp = connect(host,user,pw)
    user_input = 0

    while int(user_input) != 1:
        user_input = menu()
        options(user_input,ftp)

if __name__ == "__main__":
    main()
