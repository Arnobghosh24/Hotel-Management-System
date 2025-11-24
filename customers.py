import Main_data
import restaurant

def program(g_room):
    print("Enter Exit to Log out")
    choice=input("Enter 1 to Issue a complain. \nEnter 2 to request room cleaning services. \nEnter 3 to order food")
    while (choice not in ["1","2","3","Exit"]):
        print("Invalid Input")
        choice=input("Enter 1 to Issue a complain. \nEnter 2 to request room cleaning services. \nEnter 3 to oreder food")
    while(choice!="Exit"):
        if(choice=="1"):
            complain=input("Please write your complain")
            combined=str(g_room)+"\n"+complain
            Main_data.room_complains.append(combined)
        
        elif(choice=="2"):
            Main_data.room_cleaning.append(g_room)

        elif(choice=="3"):
            price=restaurant.food_order(g_room)
            Main_data.main_dict[g_room]["outstanding amount"]+=price
            Main_data.bill[g_room].append(price)
            
        choice=input("Enter 1 to Issue a complain. \nEnter 2 to request room cleaning services. \nEnter 3 to oreder food")
    print("\n\nLogging out \n\n\n\n")
        