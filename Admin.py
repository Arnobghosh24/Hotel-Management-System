import Main_data
import Login_credentials_data as login
import admin_only_data

import numpy as np
#changing price
def change_price ():
    p_change=1
    if(p_change==1):
        while(True):
            g_room=int(input("Enter the room number to change the price"))
            while(g_room not in Main_data.main_dict.keys()):
                g_room=int(input("Invalid Input. \nEnter the room number to change the price"))
            g_price=int(input("Enter the price of the room"))
            Main_data.main_dict[g_room]["Per-Day cost"]=g_price
            p_change=int(input("Enter 1 if you want to change the price of more rooms yes else enter 0"))
            while(p_change!=1 and p_change!=0):
                p_change=int(input("Invalid Input. \nEnter 1 if yes else enter 0"))
            if(p_change!=1):
                break

#Rmoving rooms
def remove_room():
    p_change=1
    if(p_change==1):
        while(True):
            g_room=int(input("Enter the room number to remove"))
            while(g_room not in Main_data.all_rooms):
                g_room=int(input("Invalid Input. \nEnter the room number to remove"))
            Main_data.all_rooms.remove(g_room)
            del Main_data.bill[g_room]
            del Main_data.main_dict[g_room]
            choice=int(input("Enter 1 if you want to remove more rooms else enter 0"))
            while(choice!=1 and choice!=0):
                choice=input("Invalid input. \nEnter 1 if you want to remove more rooms else enter 0")
            if(choice==0):
                break
    

#Adding rooms
def add_rooms():
    p_change=1
    if(p_change==1):
        while(True):
            g_room=int(input("Enter the room number to add"))
            while(g_room in Main_data.all_rooms):
                g_room=int(input("Invalid Input. \nEnter the room number to add"))
            Main_data.all_rooms.append(g_room)
            price=int(input("Enter the price of the room"))
            Main_data.main_dict[g_room]={"Customer Name":"NA","Occupied":False,"Date-In":"NA","Phone number":"0","Date-Out":"NA","Verification ID type":"NA","ID number":"NA","outstanding amount":0,"Per-Day cost":price}
            Main_data.bill[g_room]=[]
            choice=int(input("Enter 1 if you want to add more rooms else enter 0"))
            while(choice!=1 and choice!=0):
                choice=input("Invalid input. \nEnter 1 if you want to remove more rooms else enter 0")
            if(choice==0):
                break

    
#Room intialising
def rooms_intializing (floor,room):
    
    price=int(input("Enter the price of the rooms"))
    i=0
    while (i<=floor):
        j=1
        print("In Floor",i,end="\t")
        while(j<=room):
            r=i*100+j
            print(r,end=" ")
            Main_data.all_rooms.append(r)
            j+=1
        print()
        i+=1

    Main_data.all_rooms.sort()
    
    n=len(Main_data.all_rooms)
    room_a=np.array(Main_data.all_rooms)
    i=0
    while(i<n):
        r=room_a[i]
        Main_data.main_dict[r]={"Customer Name":"NA","Occupied":False,"Date-In":"NA","Phone number":"0","Date-Out":"NA","Verification ID type":"NA","ID number":"NA","outstanding amount":0,"Per-Day cost":price}
        Main_data.bill[r]=[]
        i+=1
            

def id_password():
    login.admin_userid="admin"
    login.admin_password=input("Enter the password for admin")

    name=input("Enter the name of receptionist")
    reception_userid=input("Enter the user id for receptionist")
    reception_password=input("Enter the password for receptionist")
    login.reception_credentials[name]={"userid":reception_userid,"Password":reception_password}

    s_name=input("Enter the name of Security person")
    security_userid=input("Enter the user id for Security")
    security_password=input("Enter the password for Security")
    login.security_credentials[name]={"userid":security_userid,"Password":security_password}

    c_name=input("Enter the name of room cleaning person")
    r_c_userid=input("Enter the user id for room cleaning")
    r_c_password=input("Enter the password for room cleaning")
    login.cleaning_credentials[name]={"userid":r_c_userid,"Password":r_c_password}
    
    
    log_choice=int(input("Enter 1 to see log in credentals else 0"))
    while(log_choice!=0 and log_choice!=1):
        log_choice=int(input("Invalid Input. \nEnter 0 to see log in credentals else 0"))
    if(log_choice==1):
        print(f"\n\nAdmin User Id-{login.admin_userid} \nAdmin password-{login.admin_password}\n")

        print("\n")
        
        for x in login.reception_credentials.keys() :
            print(f"Reception used Id-{login.reception_credentials[x]["userid"]} \nReception password-{login.reception_credentials[x]["Password"]} \n")

        print("\n")
        
        for x in login.security_credentials.keys() :
            print(f"Security used Id-{login.security_credentials[x]["userid"]} \nSecurity password-{login.security_credentials[x]["Password"]}\n")

        print("\n")
        
        for x in login.cleaning_credentials.keys() :
            print(f"Cleaning used Id-{login.cleaning_credentials[x]["userid"]} \nCleaning password-{login.cleaning_credentials[x]["Password"]}\n")

        print("\n")
        
        for x in login.room_password.keys():
            print(f"The room number {x} \n room password {login.room_password[x]} \n")

def edit_credentials():
    print("Enter 1 to edit admin password.")
    print("Enter 2 to add reception credentials. \nEnter 3 to edit reception credntials. \nEnter 4 to delete reception credentials.")
    print("Enter 5 to add Security credentials. \nEnter 6 to edit Security credntials. \nEnter 7 to delete Security credentials.")
    print("Enter 8 to add room cleaning credentials. \nEnter 9 to edit room cleaning credntials. \nEnter 10 to delete room cleaning credentials.")
    print("Enter 11 to edit a room's password")

    t=[1,2,3,4,5,6,7,8,9,10,11]
    
    edit=int(input())
    while(edit not in t):
        print("Invalid input.")
        print("Enter 1 to edit admin password.")
        print("Enter 2 to add reception credentials. \nEnter 3 to edit reception credntials. \nEnter 4 to delete reception credentials.")
        print("Enter 5 to add Security credentials. \nEnter 6 to edit Security credntials. \nEnter 7 to delete Security credentials.")
        print("Enter 8 to add room cleaning credentials. \nEnter 9 to edit room cleaning credntials. \nEnter 10 to delete room cleaning credentials.")
        print("Enter 11 to edit a room's password")
        edit=int(input())
        
    if(edit==1):
        login.admin_password=input("Enter the password for admin")
        
    elif(edit==2):
        name=input("Enter the name of receptionist")
        if(name in login.reception_credentials.keys()):
            print("Invalid credentials")
        else:
            reception_userid=input("Enter the user id for reception")
            reception_password=input("Enter the password for reception")
            login.reception_credentials[name]={"userid":reception_userid,"Password":reception_password}
    elif(edit==3):
        name=input("Enter the name of receptionist")
        if(name in login.reception_credentials.keys()):
            reception_userid=input("Enter the user id for reception")
            reception_password=input("Enter the password for reception")
            login.reception_credentials[name]={"userid":reception_userid,"Password":reception_password}
        else:
            print("Invalid credentials")

    elif(edit==4):
        name=input("Enter the name of receptionist")
        if(name in login.reception_credentials.keys()):
            del login.reception_credentials[name]
        else:
            print("Invalid Credentials")

    elif(edit==5):
        name=input("Enter the name of Security")
        if(name in login.security_credentials.keys()):
            print("Invalid credentials")
        else:
            security_userid=input("Enter the user id for security")
            security_password=input("Enter the password for security")
            login.security_credentials[name]={"userid":security_userid,"Password":security_password}
    elif(edit==6):
        name=input("Enter the name of security")
        if(name in login.security_credentials.keys()):
            security_userid=input("Enter the user id for security")
            security_password=input("Enter the password for security")
            login.security_credentials[name]={"userid":security_userid,"Password":security_password}
        else:
            print("Invalid credentials")

    elif(edit==7):
        name=input("Enter the name of security")
        if(name in login.security_credentials.keys()):
            del login.security_credentials[name]
        else:
            print("Invalid Credentials")

    elif(edit==8):
        name=input("Enter the name of cleaning staff")
        if(name in login.cleaning_credentials.keys()):
            print("Invalid credentials")
        else:
            cleaning_userid=input("Enter the user id for cleaning staff")
            cleaning_password=input("Enter the password for cleaning staff")
            login.cleaning_credentials[name]={"userid":cleaning_userid,"Password":cleaning_password}
    elif(edit==9):
        name=input("Enter the name of cleaning staff")
        if(name in login.cleaning_credentials.keys()):
            cleaning_userid=input("Enter the user id for cleaning staff")
            cleaning_password=input("Enter the password for cleaning staff")
            login.cleaning_credentials[name]={"userid":cleaning_userid,"Password":cleaning_password}
        else:
            print("Invalid credentials")

    elif(edit==10):
        name=input("Enter the name of cleaning staff")
        if(name in login.cleaning_credentials.keys()):
            del login.cleaning_credentials[name]
        else:
            print("Invalid Credentials")

    elif(edit==11):
        g_room=int(input("Enter the number of the room"))
        if(g_room in Main_data.room_password.keys()):
            password=input("Enter the password of the room")
            Main_data.room_password[g_room]=password
        else:
            print("Invalid details")

def print_credentials():
    if(True):
        print(f"\n\nAdmin User Id-{login.admin_userid} \nAdmin password-{login.admin_password}\n")

        print("\n")
        
        for x in login.reception_credentials.keys() :
            print(f"Reception used Id-{login.reception_credentials[x]["userid"]} \nReception password-{login.reception_credentials[x]["Password"]} \n")

        print("\n")
        
        for x in login.security_credentials.keys() :
            print(f"Security used Id-{login.security_credentials[x]["userid"]} \nSecurity password-{login.security_credentials[x]["Password"]}\n")

        print("\n")
        
        for x in login.cleaning_credentials.keys() :
            print(f"Cleaning used Id-{login.cleaning_credentials[x]["userid"]} \nCleaning password-{login.cleaning_credentials[x]["Password"]}\n")

        print("\n")
        
        for x in login.room_password.keys():
            print(f"The room number {x} \n room password {login.room_password[x]} \n")
            

def initialize_food():
    print("Enter Done to finish the menu.")
    food=input("Enter the food item")
    while(food!="Done"):
        price=int(input(f"Enter the price of {food}"))
        Main_data.food_menu[food]=price
        food=input("Enter the food item")

    print("the food menu is-")
    for x in Main_data.food_menu.keys():
        print(x,"\t",Main_data.food_menu[x])

def edit_food_menu():
    choice=int(input("Enter 1 if you want to add an item. \nEnter 2 if you want to delete an item. \nEnter 3 if you want to edit the price of an item"))
    while(choice!=1 and choice!=2 and choice!=3):
        choice=int(input("Invalid Output. \n\nEnter 1 if you want to add an item. \nEnter 2 if you want to delete an item. \nEnter 3 if you want to edit an item"))

    if(choice==1):
        item=input("Enter the item name")
        price=int(input("Enter the price of the item"))
        if(item not in Main_data.food_menu.keys()):
            Main_data.food_menu[item]=price
        else:
            print("The item is already listed in the menu")

    elif(choice==2):
        item=input("Enter the item name")
        if(item in Main_data.food_menu.keys()):
            del Main_data.food_menu[item]
        else:
            print("The item is not listed in the menu")

    elif(choice==3):
        item=input("Enter the item name")
        price=int(input("Enter the price of the item"))
        if(item in Main_data.food_menu.keys()):
            Main_data.food_menu[item]=price
        else:
            print("The item is not listed in the menu")


    


#Real Program
def admin():
    print("\nEnter 1 to initialize login credentials of reception and admin.  \nEnter 2 to initialize all the rooms. \nEnter 3 to remove a room. \nEnter 4 to add rooms. \nEnter 5 to change price of a room. \nEnter 6 to edit log in credentials. \nEnter 7 to see all log in credentials. \n Enter 8 to initialize the food menu. \nEnter Exit to Log out. ")
    choice=input()
    while(choice!="Exit"):
        if(choice=="1"):
            id_password()
                
        elif(choice=="2"):
            floors=int(input("Enter the total number of Floors in the hotel"))
            rooms=int(input("Enter the total number of Rooms in each floor"))
            rooms_intializing(floors,rooms)
            
        elif(choice=="3"):
            remove_room()
            
        elif(choice=="4"):
            add_rooms()
            
        elif(choice=="5"):
            change_price()

        elif(choice=="6"):
            edit_credentials()

        elif(choice=="7"):
            print_credentials()

        elif(choice=="8"):
            initialize_food()


        print("\nEnter 1 to initialize login credentials of reception and admin.  \nEnter 2 to initialize all the rooms. \nEnter 3 to remove a room. \nEnter 4 to add rooms. \nEnter 5 to change price of a room. \nEnter 6 to edit log in credentials. \nEnter 7 to see all log in credentials. \n Enter 8 to initialize the food menu. \nEnter Exit to Log out. ")
        choice=input()

    print("\n\nLoging out \n\n\n")

    