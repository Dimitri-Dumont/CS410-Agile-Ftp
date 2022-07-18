# from ftplib import FTP
import pysftp 
import os  #used to list local directory/files

def connect(host, port, user,pw):
    #ignore known_hosts check, we can remove these two lines later
    cnOpts= pysftp.CnOpts()
    cnOpts.hostkeys = None
    with pysftp.Connection(host,port,user,pw,cnOpts) as sftp:
        if(sftp):
            print('Connected to SFTP server.')
        else:
            print('Connection not successful')
    return sftp

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
#I'm not sure how to disconnect without connecting first and storing that in a variable as sftp so we can close it.
#I also dont know if a connection is persistant 
def disconnect(sftp):
    #ignore known_hosts check, we can remove these two lines later
    cnOpts= pysftp.CnOpts()
    cnOpts.hostkeys = None
    if sftp:
        sftp.close()
        print('Disconnected to SFTP server.')
    else:
        print('Connection not successful')

#user inputs number then selects from the different options listed in the menu
def options(user_input, sftp):
    if user_input == 1:
       disconnect(sftp) 
    elif user_input == 2:
       listDir(sftp) 
    elif user_input == 3:
       path = input("Enter path: ")
       listDirLocal(path) 


#this just lists the files in current directory, not all directories
def listDir(sftp):
    files = sftp.listdir_attr(".")
    for f in files:
        print(f)
#list local files/directories 
def listDirLocal(path):
    with os.scandir(path) as it:
        for entry in it:
            if not entry.name.startswith('.'):
                print(entry.name)
def main():
    #connect immediately then catch the sftp object to interact with the other functions
    # print("Lets start by obtaining some information, please enter: ")
    # host = input("Enter your host address: ")
    # user = input("Enter your username: ")
    # port = input("Enter the port: ") #usually port 22, not sure we need to specify this
    # pw = input("Enter your password: ")
    # sftp = connect(host,user,port,pw)
    sftp = 2 
    user_input = menu() #Find out what user wants to do
    options(user_input,sftp) #Select what they want 
if __name__ == "__main__":
    main()