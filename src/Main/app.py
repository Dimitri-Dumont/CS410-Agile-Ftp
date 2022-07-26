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
    FILENAME = 'syllabus.pdf'
    # sftp.cwd('/')

    with open(FILENAME, 'wb') as f:
        sftp.retrbinary('RETR' + FILENAME, f.write)

def main():
    # public ip once server is running remotley:
        #host = '67.160.144.238'

    print("Defaulting to local server for testing")
    host = 'localhost'
    user = 'Test'
    pw = 'RubberDuck'
    ftp = connect(host,user,pw)
    user_input = menu()
    options(user_input,ftp)

if __name__ == "__main__":
    main()
