ph_direct = dict()

def ph_no_add(x):
    print("***Welcome to the phone directory***")
    add_name=input("please enter your name to: ")
    add_no=input("please enter your  phone number: ")

    x=ph_direct.setdefault(add_name,add_no)
    print(f"{add_name}'your name and number have been added to the directory...")


def ph_direct_show(x):
    person_count=len(x)
    print(f"Number of entries in the directory: {person_count}")


    print("\n***Phone Directory***")
    for i,j in x.items():
        print(i,":",j)
    input("Do you want continiue")
def no_del(x):
    print("\nDelete person")
    deleted_person=input("enter the name of the person you want to delete: ")
    x =  ph_direct.pop(deleted_person)
    input("Do you want continiue")

while True:
    print("\n***Welcome to Directory***")
    print("Pic a  number to perform an action:")
    action_directory=int(input("1-Add\n2-Delete\n3-Show Directory\n"))

    if  action_directory==1:
        ph_no_add(ph_direct)
    elif action_directory==2:
        no_del(ph_direct)
    elif action_directory==3:
        ph_direct_show(ph_direct)
    else:
        print("Please Enter an number")    

