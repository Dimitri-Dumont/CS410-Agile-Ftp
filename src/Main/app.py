from ftplib import FTP
import os

def menu():
    print("1. Disconnect from SFTP server")
    print("2. List directories & files on server")
    print("3. List directories & files on local machine")
    print("4. Get file from remote server")
    print("5. List directories and files on remote server")
    print("6. Get multiple files")
    print("7. Delete file from remote server ")

    user_input = input("Enter number of what you would like to do:\n")
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

def getFile(sftp):
    # FILENAME = '/Users/xreed/Desktop/FTP/syllabus.pdf'
    FILENAME = "SampleText.txt"
    # sftp.cwd("/Users/xreed/Desktop/FTP/")
    sftp.cwd("My Documents")
    print(sftp.pwd())
    print(sftp.dir())


    with open(FILENAME, 'wb') as fp:
        sftp.retrbinary('RETR ' + FILENAME, fp.write)
        # sftp.retrlines('RETR ' + FILENAME, f.write)

def main():
    '''
    print("Defaulting to local server for testing")
    host = 'localhost'
    user = 'Test'
    pw = 'RubberDuck'
    '''
    host = '66.220.9.50'
    user = 'agile_class'
    pw = 'password123!'
    ftp = connect(host,user,pw)
    user_input = menu()
    options(user_input,ftp)

if __name__ == "__main__":
    main()
