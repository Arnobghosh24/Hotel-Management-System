import Main_data

def program():
    print("Enter Exit to Log out")
    choice=input("Enter 1 to see how many rooms to clean. \nEnter 2 to see all the rooms to clean. \nEnter 3 to print which room to clean right now. \nEnter 4 to mark your job")
    while(choice not in ["1","2","3","4","Exit"]):
        choice=input("Invalid input")
    while(choice!="Exit"):
        if(choice=="1"):
            print(len(Main_data.room_cleaning))

        elif(choice=="2"):
            print(Main_data.room_cleaning)

        elif(choice=="3"):
            if(len(Main_data.room_cleaning)>0):
                print(Main_data.room_cleaning[0])
            else:
                print("Enjoy \nNo room to clean right now")

        elif(choice=="4"):
            g_room=int(input("Enter the room number you have cleaned"))
            if(g_room in Main_data.room_cleaning):
                Main_data.room_cleaning.remove(g_room)
            else:
                print("Wrong Input")
        
        print("Enter Exit to Log out")
        choice=input("Enter 1 to see how many rooms to clean. \nEnter 2 to see all the rooms to clean. \nEnter 3 to print which room to clean right now. \nEnter 4 to mark your job")
        while(choice not in ["1","2","3","4","Exit"]):
            choice=input("Invalid input")

    print("\n\nLogging Out\n\n\n\n")
            
