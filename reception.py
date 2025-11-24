import random
import numpy as np
from datetime import datetime

import Main_data

def Reception ():
    print("\n\n\nMenu:")
    choice=input("Enter 1 to Check in new guest.\nEnter 2 to extend the stay of an existing Guest. \nEnter 3 to check-out a Guest.\nEnter 4 to access the details of the room. \nEnter 5 to see complain list. \nEnter 6 to mark a complain as resolved. \nEnter Exit to Log out\n\n")
    while(choice!="Exit"):
        if(choice=="1"):
            name=input("Enter the Guest name")
            room_ch=input((f"Does {name} has any specific room preference Yes or NO"))
            g_room=0
            while(room_ch=="Yes"):
                r_ch=int(input("Enter the room number"))
                if((Main_data.main_dict[r_ch])["Occupied"]):
                    print(f"Sorry, {name} the room is already occupied")
                    room_ch=input((f"Does {name} has any specific room preference left or should we allot you a random room? \nEnter Yes for specific room else Enter No"))
                elif(r_ch in Main_data.room_cleaning):
                    print(f"Sorry, {name} the room is not cleaned")
                    room_ch=input((f"Does {name} has any specific room preference left or should we allot you a random room? \nEnter Yes for specific room else Enter No"))
                else:
                    g_room=r_ch
                    break
            if(room_ch=="No"):
                g_room=random.choice(Main_data.all_rooms)
                while(Main_data.main_dict[g_room]["Occupied"] or g_room in Main_data.room_cleaning):
                    g_room=random.choice(Main_data.all_rooms)
            Main_data.main_dict[g_room]["Customer Name"]=name
            phone=input(f"Enter the phone number of {Main_data.main_dict[g_room]["Customer Name"]}.")
            while(len(phone)!=10):
                phone=input(f"Invalid input. \nEnter the phone number of {Main_data.main_dict[g_room]["Customer Name"]} .")
            Main_data.main_dict[g_room]["Phone number"]=phone
            Main_data.main_dict[g_room]["Occupied"]=True
            time=datetime.now()
            c_now=time.strftime("%d/%m/%Y")
            print("\nToday is",c_now,end="\n\n")
            Main_data.main_dict[g_room]["Date-In"]=input("Enter the date for Check in")
            Main_data.main_dict[g_room]["Date-Out"]=input("Enter the date for Check out")
            days=int(input("Enter the number of days the Guest will live in out hotel"))
            Main_data.main_dict[g_room]["Verification ID type"]=input("Enter the verification id type used")
            Main_data.main_dict[g_room]["ID number"]=input("Enter the verification id credentials used for Verification")
            y=str(Main_data.main_dict[g_room]["Per-Day cost"]*days)
            y="Room Cost "+y
            paid=int(input(f"{y} \nEnter the amount {name} has payed."))
            Main_data.main_dict[g_room]["outstanding amount"]=(Main_data.main_dict[g_room]["Per-Day cost"]*days)-paid
            Main_data.bill[g_room].append(y)
            psw=input(f"Enter the password {name} want for the hotel's online facilities")
            Main_data.room_password[g_room]=psw

        elif(choice=="2"):
            g_room=int(input("Enter the room for check out"))
            while(Main_data.main_dict[g_room]["Occupied"]==False):
                g_room=int(input("Invalid input. \nEnter the room for check out"))
            time=datetime.now()
            c_now=time.strftime("%d/%m/%Y")
            print("\nToday is",c_now,end="\n\n")
            print("Expected check out date was",Main_data.main_dict[g_room]["Date-Out"])

            fl=int(input("Enter 1 if the guest overstayed else enter 0"))
            
            if(fl==1):
                print(f"Kindly enter the number of extra days {Main_data.main_dict[g_room]["Customer Name"]} stayed in the hotel")
                days=int(input())
                y=str(Main_data.main_dict[g_room]["Per-Day cost"]*days)
                y="Extra days room Cost "+y
                Main_data.main_dict[g_room]["outstanding amount"]=Main_data.main_dict[g_room]["outstanding amount"]+(days*Main_data.main_dict[g_room]["Per-Day cost"])
                
        
            while(Main_data.main_dict[g_room]["outstanding amount"]!=0):
                print("There is an outstanding amount for the stay in the hotel. \nKindly clear are the remaing dues.\nRemaining amount=",Main_data.main_dict[g_room]["outstanding amount"])
                paid=int(input())
                Main_data.main_dict[g_room]["outstanding amount"]=Main_data.main_dict[g_room]["outstanding amount"]-paid

            choice=int(input("Do you want to see the bill? \nEnter 1 to see else 0"))
            if(choice==1):
                print(Main_data.bill[g_room])
            print(f"Thank you for staying with us. We hope your visit was relaxing and enjoyable, and we look forward to seeing you again soon!")
            price=Main_data.main_dict[g_room]["Per-Day cost"]

            Main_data.main_dict[g_room]={"Customer Name":"NA","Occupied":False,"Date-In":"NA","Date-Out":"NA","Verification ID type":"NA","ID number":"NA","outstanding amount":0,"Per-Day cost":price}
            Main_data.bill[g_room]=[]
            Main_data.room_cleaning.append(g_room)
            del Main_data.room_password[g_room]

        elif(choice=="3"):
            g_room=int(input("Enter the room for check out"))
            while(Main_data.main_dict[g_room]["Occupied"]==False):
                g_room=int(input("Invalid input. \nEnter the room for check out"))

            print(f"Right now the check-out date is{Main_data.main_dict[g_room]["Date-Out"]}")
            ch=int(input("So dou you really want to change the check out dates? \nEnter 1 to change else press 2"))
            if(ch==1):
                change=input("Enter the check out dates")
                days=int(input("Enter the extra number of days the Guest will be staying in the hotel"))
                Main_data.main_dict[g_room]["outstanding amount"]=Main_data.main_dict[g_room]["outstanding amount"]+(Main_data.main_dict[g_room]["Per-Day cost"]*days))
                Main_data.main_dict[g_room]["Date-Out"]=change
                rem=(Main_data.main_dict[g_room]["Per-Day cost"]*days)
                y="Extra days bill is"+str(rem)
                Main_data.bill[g_room].append(y)
            elif(ch==2):
                print("Okay no changes will be done at the check out dates")
        elif(choice=="4"):
            g_room=int(input("Enter the room no to get the details of the room"))
            while(g_room not in Main_data.main_dict.keys()):
                g_room=int(input("Invalid input. \nEnter the room no to get the details of the room."))
            for i in Main_data.main_dict[g_room].keys():
                print(i,Main_data.main_dict[g_room][i])

        elif(choice=="5"):
            print(Main_data.room_complains)

        elif(choice=="6"):
            print(Main_data.room_complains)
            n=int(input("Enter the position of the room complain"))
            n-=1
            print(Main_data.room_complains[n])
            choice=int(input("Enter 1 if this is the complain you want to mark as done else enter 0."))
            while(choice!=1 and choice!=0):
                choice=int(input("Invalid input. \nEnter 1 if this is the complain you want to mark as done else enter 0."))
            while(choice==0):
                print(Main_data.room_complains)
                n=int(input("Enter the position of the room complain"))
                n-=1
                print(Main_data.room_complains[n])
                choice=int(input("Enter 1 if this is the complain you want to mark as done else enter 0."))
                while(choice!=1 and choice!=0):
                    choice=int(input("Invalid input. \nEnter 1 if this is the complain you want to mark as done else enter 0."))

            Main_data.room_complains.pop(n)
            
        
        else:
            choice=input("Invalid Input. \nEnter a valid choice")
            continue
            
        choice=input("\n\n\nEnter 1 to Check in new guest.\nEnter 2 to extend the stay of an existing Guest. \nEnter 3 to check-out a Guest.\nEnter 4 to access the details of the room. \nEnter exit to exit the program\n\n")

    print("\n\nLogging Out \n\n\n")