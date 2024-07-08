#Contact Book
'''
Contact Information: Store name, phone number, email, and address for each contact.
Add Contact: Allow users to add new contacts with their details.
View Contact List: Display a list of all saved contacts with names and phone numbers.
Search Contact: Implement a search function to find contacts by name or phone number.
Update Contact: Enable users to update contact details.
Delete Contact: Provide an option to delete a contact.
'''
cb=[]
def add():
    n=input("Name: ")
    p=int(input("Phone No.: "))
    m=input("Email ID: ")
    a=input("Address: ")
    c=[n,p,m,a]
    cb.append(c)
def view():
    for i in cb:
        print('Name: ',i[0],'\n','Phone no.: ',i[1],'\n','Email: ',i[2],'\n','Address: ',i[3])
def search():
    s=input('Enter search info: ')
    for i in cb:
        if s in i[0] or s in str(i[1]) or s in i[2] or s in i[3]:
            print('Name: ',i[0],'\n','Phone no.: ',i[1],'\n','Email: ',i[2],'\n','Address: ',i[3])
def update():
    s=input('Enter contact for input: ')
    for i in cb:
        if s in i[0] or s in str(i[1]) or s in i[2] or s in i[3]:
            print('Name: ',i[0],'\n','Phone no.: ',i[1],'\n','Email: ',i[2],'\n','Address: ',i[3])
            print("0-Name\n1-Phone no.\n2-Email ID\n3-Address")
            u=int(input("Enter category of change: "))
            U=input("Enter updated detail: ")
            i[u]=U
            print("Contact Updated")
def delete():
    s=input('Enter contact for input: ')
    for i in cb:
        if s in i[0] or s in str(i[1]) or s in i[2] or s in i[3]:
            cb.pop(cb.index(i))
print("CONTACT BOOK")
c=''
while c!='n':
    print("1.Add a new Contact\n2. View All\n3. Search\n4. Update existing contact\n5. Delete a Contact")
    s=int(input())
    match s:
        case 1:
            t_pending, t_complete=[], []
            add()
        case 2:
            view()
        case 3:
            search()
        case 4:
            update()
        case 5:
            delete()
        case _:
            print("Incorrect input! Re-Enter your choice")
    print("To Continue: y\n To End: n")
    c=input().lower()
