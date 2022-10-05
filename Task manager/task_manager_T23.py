#========= CAPSTONE PROJECT ============#


#====Import Libraries====

from datetime import date, datetime

#Defining functions
def reg_user():
    user_registered = False
    while user_registered == False:
        password_n = input("Please enter your new password:\n")
        password_c = input("Please confirm your new password:\n")

#If the passwords match it will break out of the loop
        if password_n == password_c:
            with open('user.txt','a') as f:
                f.write('\n' + username_n + ',' + ' ' + password_n)
                print("New user registered")
                user_registered = True
                break

#else it will continue the loop
        else:
            user_registered = False
            print("The passwords you've entered do not match")
            continue
            f.close()

def add_task():
#opening file
    task_file = open('tasks.txt','a')

#Requesting inputs from user and writing it to file
    username_a =input("Please enter the username of the person who the task is assigned to:\n")
    task_a = input("Please enter the title of the task:\n")
    description_a = input("Please enter a description of the task: \n")
    duedate_a = input("Please enter the due date of the task (Enter with the following format: 10 Oct 2019):\n")
    task_file.write(username_a + ", " + task_a + ", " + description_a + ", "
                    + str(date.today().strftime("%d %b %Y")) + ", " + duedate_a + ", No\n")
    task_file.close()
    print("Your task has been successfully entered")

def view_all():
    task_file_2 = open('tasks.txt','r+') #opening file

#Creating a for loop in order to print each line of the task file in the desired format
    for line in task_file_2:
        tasklist = line.split(",")
        print(u'\u2500' * 50 + "\n" + "Task:\t\t"+ tasklist[1]+ "\n" + "Assigned to:\t"+ tasklist[0]+
                    "\n" + "Date Assigned:\t" + str(date.today()) + "\n" + "Due Date:\t" + tasklist[4]
                + "\n" + "Task Complete?:\t" + tasklist[5] + "\n" + "Task Description:\n"
                + tasklist[2] + "\n")
    task_file_2.close()

def view_mine():
#Requesting user's name        
    task_file_3 = open('tasks.txt','r+')
    file_contents = task_file_3.readlines() # We are reading the content of the files (strings) and writing it to a variable called file contents
#For loop to print each of the tasks matching the username
    has_tasks = False #Declaring has tasks false
    user_task_list = [] #Creating a list where we'll store this specific user's tasks
    task_count = 0 #Creating a counter
    for line in file_contents:
        tasklist = line.replace("\n", "").split(", ") #creating a list of each line in file contents
        if username == tasklist[0]:
            user_task_list.append(tasklist) #appends the asks for that specific user
            has_tasks = True #Has tasks will be equal to true
            task_count += 1 #Setting a counter for task count
#printing all the users tasks
            print(f'''
Task Count:    {task_count}
Task:          {tasklist[1]}
Assign to:     {tasklist[0]}
Date Assigned: {tasklist[3]}
Due Date:      {tasklist[4]}
Task Complete?: {tasklist[5]}
Task Description:
{tasklist[2]}\n''')

#Creating variable for number request from user, -1 because index starts at 0
    assigned_number = int(input("Enter the number of the task you would like to edit or press -1 to go back to the main menu:\n")) -1
    if assigned_number == -2: #because we minused one above
        pass #Goes back to menu

    else:
        selected_task = user_task_list[assigned_number] #The selected task is the task in user task list at the index of assisgned number
        selected_task_all_index = file_contents.index(", ".join(selected_task)) #makes it a string
        edit_status = selected_task[-1].replace("\n", "")
        if edit_status == "No":
            edit_task = input("1. To change the due date\n"\
                            "2. To change the username\n"\
                            "3. To mark the task as complete\n"\
                            "Selection: ")
    #printing selected task   
            print(f'''
    Task:          {selected_task[1]}
    Assign to:     {selected_task[0]}
    Date Assigned: {selected_task[3]}
    Due Date :      {selected_task[4]}
    Task Complete?:{selected_task[5]}
    Task Description:
    {selected_task[2]}\n''')
            if edit_task == "1":
                selected_task[4] = input("What is the new due date: ") #changing the due date
                print(file_contents)

            elif edit_task == "2":
                selected_task[0] = input("Reassign task to: ") #Reassigning the task

            elif edit_task == "3":
                selected_task[-1] = "Yes\n"         #changing status
            
            file_contents[selected_task_all_index] = ", ".join(selected_task) #dont get this
            with open('tasks.txt',"w") as write_file:
                for line in file_contents:
                    write_file.write(line)
                            
        else:
            print("You can not edit a completed task")   #error message        
                 
    if not has_tasks:
        print("You have no tasks") #if user not in tasks file

def reports():
#opening files 
    task_file_5 = open('tasks.txt','r') 
    task_overview =  open ('task_overview.txt', 'w')
    user_overview = open('user_overview.txt', 'w')

#Defining variables
    task_count_total= 0
    completed_task_count = 0
    uncompleted_task_count = 0
    uncompleted_overdue = 0
    user_count = 0
    user_task_count = 0
    user_task_complete = 0
    user_task_incomplete= 0
    user_task_overdue= 0
    total_task_count = 0

#Setting up a for loop 
    for line in task_file_5:
        task_count_total += 1 #adds to the task count
        task_list = line.split(',') #split string into list
        today = date.today() #Going to use to determine if overdue 
        task_due_date = datetime.strptime(task_list[-2][1:],'%d %b %Y' ).date() #converting our time format
        if task_list[-1] == ' Yes\n':
            completed_task_count += 1 #adding to completed task count

        elif task_list[-1] == ' No\n':
            uncompleted_task_count += 1 #adding to incomplete task count
           
        
            if task_due_date  <today: #determining if overdue
                uncompleted_overdue += 1 #adding to overdue task counts

#defining percentage variables
    percentage_uncompleted = ((round(uncompleted_task_count/task_count_total,2))*100)
    percentage_overdue = ((round(uncompleted_overdue/task_count_total,2))*100)

#Writing to task overview txt
    task_overview.write("\n The total number of tasks in the task manager is" + " "+ (str(task_count_total))\
                + "\n The total number of completed tasks in the task manager is" + " " + (str(completed_task_count))\
                + "\n The total number of incomplete tasks in the task manager is" + " " + (str(uncompleted_task_count))\
                + "\n The total number of incomplete overdue tasks is" + " " +  (str(uncompleted_overdue))\
                + "\n The percentage of uncompleted tasks is" + " " + (str(percentage_uncompleted))\
                + "\n The percentage of overdue tasks is" + " " +(str(percentage_overdue))
                )

    with open("user.txt", "r") as f: # opening the user txt file
        user_contents = f.readlines() #reading contents into variable containing strings
        username_list = [] # Creating a list of usernames
        
        for line in user_contents:
            line = line.split(", ") #splitting string into a list
            username_list.append(line[0]) #Then appending first item in list to username list
    
    user_overview.close() #closing it so I can open it for appending

    with open('user_overview.txt', 'w') as user_overview:
#Total number of users registered
        for user in username_list:
            user_count+=1

#Total task count
        task_file_5.seek(0)
        for task in task_file_5:
            total_task_count += 1
#Creating a nested for loop to loop over the usernames and the tasks
        for user in username_list:
            user_task_count = 0
            task_file_5.seek(0) #Going back to the beginning of the file
            for task in task_file_5:
                task = task.split(', ') #spliting each line of string into a list
                if task[0] == user: # matching task to user
                    user_task_count += 1
                    if task[-1] == " Yes\n":
                        user_task_complete += 1
# For tasks that are incomplete findin out if they are overdue and adding to counters
                    elif task[-1] == " No\n": 
                        user_task_incomplete += 1
                        if task_due_date>today:
                            user_task_overdue += 1

#Creating so that we dont get a divisible by 0 error         
            if user_task_count == 0: # 
                user_task_percentage = 0
                user_complete_percentage = 0
                user_incomplete_percentage = 0
                user_overdue_percentage = 0

 #Creating percentage variables and writing to user overview file           
            else:
                user_task_percentage = (user_task_count/total_task_count)*100
                user_complete_percentage = (user_task_complete/user_task_count)*100
                user_incomplete_percentage = (user_task_incomplete/user_task_count)*100
                user_overdue_percentage = (user_task_overdue/user_task_count)*100
            user_overview.write(f"\n\n\t\t{user}\n  The total number of tasks for this user is:" + " " +str(user_task_count)\
                        + "\n The percentage of the total number of tasks assigned to this user is:" + " " + str(user_task_percentage)
                        + "\n The percentage of assigned tasks completed is:" + " " + str(user_complete_percentage)\
                        + "\n The percentage of assigned tasks that are incomplete is:" + " " + str(user_incomplete_percentage)\
                        + "\n The percentage of assigned tasks that are overdue is:" + " " + str(user_overdue_percentage))


def display_stats():

    reports()
    with open("user_overview.txt", "r") as user_overview_2: #opening file for reading
        print("User Overview:")
        for line in user_overview_2:
            print(line) # printing each line in the file

    print("\n")
    with open("task_overview.txt", "r") as task_read: #same as above
        print("Task Overview")
        for line in task_read:
            print(line)


#====Login Section====

print("Login")

while True:
    print("\nUsername:")
    username = input("Please enter your username:\n")
    print("\nPassword:")
    password = input("Please enter your password:\n")
    login_credentials = str(username + ',' + ' ' + password)

    with open('user.txt','r+') as f:
        deny_access = True
        for line in f:
            if line.replace("\n", "") == login_credentials:
                deny_access = False
                break
            
    if deny_access == True:
        print("\nIncorrect username or password\nPlease Try again")
        continue

    elif deny_access == False:
        print("Welcome to the menu")
        break

#====Menu Section====

if username == "admin":
    menu_statement = '''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - Display statistics
e - Exit
: '''


else:
    menu_statement = '''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit

: '''

while True:
    menu = input(menu_statement)
    
#Checking that the username is admin

    if menu == 'r':

        if username != "admin":
            print("Access Denied: Only admin is allowed to add new users!") #denying access to users that are not admin
            continue

        elif username == "admin":
             
            while True: 
                duplicate_username = False
                username_n = input("Please enter your new username:\n")
                with open('user.txt','r+') as f:
                    for line in f:
                        user_list = line.split(",")
                        if username_n != user_list[0]:
                            pass

                        else:
                            print("Error: Username already in use, enter a different username")
                            duplicate_username = True
                            break

                if duplicate_username:
                    continue
                
                else:
                    reg_user()
                    break
                       

#Adding tasks section
    elif menu == 'a':
        add_task()

#View all section
    elif menu == 'va':
        view_all()
           
#View my tasks section
    elif menu == 'vm':
        view_mine()
    
    elif menu == 'gr':
        reports()

    elif menu == 'ds':
        display_stats()
            
#Exit option            
    elif menu == 'e':
        print('Goodbye!!!')
        exit()            

    else:
        print("You have made a wrong choice, Please Try again")


#######============ References =============#
####### https://stackoverflow.com/questions/47202331/python-username-and-password-with-3-attempts
####### https://stackoverflow.com/questions/71661961/how-can-i-check-each-line-in-a-txt-file-for-the-right-username-and-password
####### https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
