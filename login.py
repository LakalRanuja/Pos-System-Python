from os import name
import sys

__session_file__ = "db/session.db"

def __get_logged_user():
    f = open(__session_file__,"r")
    userName = f.readline()
    return userName

def viewUser():
    userName = __get_logged_user()
    print(userName)

def login(userName):
    f = open(__session_file__,"w")
    f.write(userName)
    f.close()

if __name__ == "__main__":
    arguments = sys.argv[1:]
    section = arguments[0]
    command = arguments[1]
    params = arguments[2:]
    print(section,command,params)

    if section == "user":
        if command == "login":
            login(*params)
        elif command =="view":
            viewUser()

    
