from ftplib import FTP
import os

def menu():
    print("1. Disconnect from ftp server")
    print("2. List directories & files on server")
    print("3. List directories & files on local machine")
    print("4. Get a File From Server")
    print("5. Get Multiple Files From Server ")
    print("6. Create Directory On Server")
    print("7. Delete Directory From Server")
    print("8. Upload File On Server")
    print("9. Delete File From Server")
    print("10. Upload Multiple Files On Server")

    user_input = input("Enter number of what you would like to do:\n")
    return user_input
#For some reason match doesn't work for my vscode, I'm going to change it to if/elif. You can change it back for the presentation
def options(user_input, ftp):
     if user_input == '1':
            disconnect(ftp)
     if user_input == '2':
            listDir(ftp)
     if user_input == '3':
            listDirLocal()
     if user_input == '4':
            getFile(ftp)
     if user_input == '5':
            getMultiple(ftp)
     if user_input == '6':
            createDirectory(ftp)
     if user_input == '7':
            deleteDirectory(ftp)
     if user_input == '8':
            uploadFile(ftp)
     if user_input == '9':
            deleteFile(ftp)
    #not working yet
     if user_input == '10':
            uploadMultiple(ftp)


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
    # ftp.nlst()
    # ftp.retrlines('LIST')

def listDirLocal(): # Only listing directories at the moment not files
 #   with os.scandir('C:\\') as it:
 #       for entry in it:
 #           if not entry.name.startswith('.'):
 #               print(entry)
    print("Current directory: " + os.getcwd())
    path = input("Enter path you wish to view: ")
    dir_list =os.listdir(path)
    print("Files and directories in '", path, "' :")
    print(dir_list)

def getFile(ftp):
    FILENAME = "SampleText.txt"
    ftp.cwd("My Documents")
    # print(ftp.pwd())
    # print(ftp.dir())


    with open(FILENAME, 'wb') as fp:
        ftp.retrbinary('RETR ' + FILENAME, fp.write)
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

#can't get this to work, it states "No such file or directory"
def uploadMultiple(ftp):
    print(os.getcwd())
    path = input("Enter local path to directory of the files you wish to upload: ")
    remote_path = input("Enter remote path to directory of the files you wish to upload: ")
    for root, dirs, files in os.walk(path):
        for filename in files:
            full_fname = os.path.join(root,filename)
            ftp.storbinary('STOR '+remote_path, open(full_fname, 'rb'))


def main():
    host = '66.220.9.50'
    user = 'agile_class'
    pw = 'password123!'
    ftp = connect(host,user,pw)
    user_input = menu()
    options(user_input,ftp)

if __name__ == "__main__":
    main()
