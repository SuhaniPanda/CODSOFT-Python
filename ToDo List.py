#Command-line based To-Do List application using Python, to create, update, and track their to-do lists
def create():
    print("Enter Your Tasks: \nPress (=) to finish editing")
    t=input()
    while t!='=':
        t_pending.append(t)
        t=input()
    print("Task List Created !")
        
def update():
    print("1. Add New Task\n2. Mark As Done")
    u=int(input())
    if u==1:
        print("Enter Your Tasks: \nPress (=) to finish editing")
        t=input()
        while t!='=':
            t_pending.append(t)
            t=input()
    elif u==2:
        print("Enter Completed Tasks: \nPress (=) to finish editing")
        t=input()
        while t!='=':
            if t in t_pending:
                t_pending.remove(t)
                t_complete.append(t)
            else:
                print("Task not found")
            t=input()
    else:
        print("Incorrect Input! Enter Again...")
        update()
    print("Task List Updated !")

def track():
    print("Pending Tasks")
    for i in t_pending:
        print(i)
    print("Completed Tasks")
    for i in t_complete:
        print(i)
        
print("ORGANISE YOUR DAY-TO-DAY ROUTINE")
c=''
while c!='n':
    print("1.Create a new List\n2. Update existing List\n3. Track your Progress")
    s=int(input())
    match s:
        case 1:
            t_pending, t_complete=[], []
            create()
        case 2:
            update()
        case 3:
            track()
        case _:
            print("Incorrect input! Re-Enter your choice")
    print("To Continue: y\n To End: n")
    c=input().lower()
        
