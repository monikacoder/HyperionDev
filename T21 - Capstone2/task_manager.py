
#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import date
#from colorama import Fore, Back, Style

today = date.today()


#====Login Section====
'''Read the user credentials from the provied file
'''
user_pass = {}
with open('user.txt') as f:
    for line in f.readlines():
        split_line = line.split(', ')
        user_pass[split_line[0]] = split_line[1].strip()

#In the below block check if the user provided crednetials are valid as per the file-read credentials fetched above
username = ""
password = ""
while True:
    username = input("Enter the username :")
    password = input("Enter the password :")
    if username in user_pass:
        if user_pass[username] == password:
            print("Login is successful \n")
            break
        else:
            print("Password provided was wrong")
    else:
        print(f"User {username} not found")


while True:
    #presenting the menu to the user and
    if username == "admin":
        menu = input('''Select one of the following Options below:
    r - Registering a user
    a - Adding a task
    va - View all tasks
    vm - view my task
    s - Statistics
    e - Exit
    : ''').lower()
    else :
        menu = input('''Select one of the following Options below:            
            a - Adding a task
            va - View all tasks
            vm - view my task
            e - Exit
            : ''').lower()

    if menu == 'r' and username == "admin":
        '''Register a new user by asking new username , password , and confirm-password'''
        new_username = input("Enter the new username : ")
        new_password = input("Enter the new password : ")
        new_password_confirm = input("Confirm the new password : ")
        if new_password == new_password_confirm:
            with open('user.txt','a') as f:
                f.write("\n" + new_username + ", " + new_password)
        else:
            print("Password does not match with confirm password")
    elif menu == 's' and username == "admin":
        print("------------------Displaying Statistics------------")
        with open('tasks.txt', 'r') as f:
            print(f"Total number of tasks is    :{str(len(f.readlines()))}" )
        with open('user.txt', 'r') as f:
            print(f"Total number of users is    :{str(len(f.readlines()))}")
        print("--------------------------------------------------\n")

    elif menu == 'a':
        '''Add a new task to the tasks.txt by taking input from the user'''
        task_user = input("Enter the username to whom the task is assigned to :")
        task_title = input("Enter the title of the task :")
        task_description = input("Enter the description of the task :")
        task_due_date = input("Enter the due date of the task :")
        task_current_date = today.strftime("%d %b %Y")
        with open('tasks.txt','a') as f:
            f.write("\n" + task_user + ", " + task_title + ", " + task_description + ", " + task_current_date + ", " + task_due_date + ", " + "No")

    elif menu == 'va':
        '''View all the tasks from the tasks.txt for all the users'''
        print("\nDisplaying all tasks :")
        with open('tasks.txt', 'r') as f:
            for line in f.readlines():
                task_items = line.split(", ")                
                print("----------------------------------------------------------------")
                print(f"Task:                      {task_items[1]}")
                print(f"Assigned To:               {task_items[0]}")
                print(f"Date assigned :            {task_items[3]}")
                print(f"Due date :                 {task_items[4]}")
                print(f"Task complete :            {task_items[5].strip()}")
                print(f"Task description :         {task_items[2]}")
                print("----------------------------------------------------------------")

    elif menu == 'vm':
        '''View all the tasks from the tasks.txt for the logged in user'''
        print("\nDisplaying your tasks :")
        with open('tasks.txt', 'r') as f:
            for line in f.readlines():
                task_items = line.split(", ")
                if username == task_items[0]:
                    print("----------------------------------------------------------------")
                    print(f"Task:                      {task_items[1]}")
                    print(f"Assigned To:               {task_items[0]}")
                    print(f"Date assigned :            {task_items[3]}")
                    print(f"Due date :                 {task_items[4]}")
                    print(f"Task complete :            {task_items[5].strip()}")
                    print(f"Task description :         {task_items[2]}")
                    print("----------------------------------------------------------------")
        print()

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
