from datetime import datetime
import Main_data

def program():
    print("Enter 1 to check in a car. \nEnter 2 to ckeck out a car. \nEnter 3 to print car check in list. \nEnter 4 to print car check out list.\nEnter Exit to Log out")
    s_choice=input("Enter your choice")
    while(s_choice!="Exit"):
        now=datetime.now()
        if(s_choice=="1"):
            gr=int(input("Enter 1 if you are a room owner \nEnter 2 if you are a guest "))
            while(gr!=1 and gr!=2):
                gr=int(input("Invalid input. \nEnter 1 if you are a room owner \nEnter 2 if you are a guest "))
            if(gr==1):
                fl=True
                room=int(input("Enter your room number"))
                name=input("Enter your name")
                if(room not in Main_data.main_dict.keys() or Main_data.main_dict[room]["Customer Name"]!=name ):
                    print("No information found. \nAccess denied")
                    continue
                car_number=input("Enter car number")
                print("Access Granted")
                Main_data.check_in+=1
                Main_data.security_check_in[Main_data.check_in]={"Room number":room,"Name":name,"Car number":car_number,"Owner":True,"Time":now}

            elif(gr==2):
                fl=True
                room=int(input("Enter room owner's room number"))
                name=input("Enter your name")
                r_name=input("Enter room owner's name")
                if(room not in Main_data.main_dict.keys() or Main_data.main_dict[room]["Customer Name"]!=r_name ):
                    print("No information found. \nAccess denied")
                    continue
                car_number=input("Enter car number")
                print("Access Granted")
                Main_data.check_in+=1
                Main_data.security_check_in[Main_data.check_in]={"Room number":room,"Name":name,"Car number":car_number,"Owner":False,"Time":now}

                
        elif(s_choice=="2"):
            gr=int(input("Enter 1 if you are a room owner \nEnter 2 if you are a guest "))
            while(gr!=1 and gr!=2):
                gr=int(input("Invalid input. \nEnter 1 if you are a room owner \nEnter 2 if you are a guest "))
            if(gr==1):
                fl=True
                room=int(input("Enter your room number"))
                name=input("Enter your name")
                car_number=input("Enter car number")
                print("Access Granted")
                Main_data.check_out+=1
                Main_data.security_check_out[Main_data.check_out]={"Room number":room,"Name":name,"Car number":car_number,"Owner":True,"Time":now}

            elif(gr==2):
                fl=True
                room=int(input("Enter room owner's room number"))
                name=input("Enter your name")
                car_number=input("Enter car number")
                print("Access Granted")
                Main_data.check_out+=1
                Main_data.security_check_out[Main_data.check_out]={"Room number":room,"Name":name,"Car number":car_number,"Owner":False,"Time":now}

        elif(s_choice=="3"):
            i=1
            print("S.no \t Room number \t Name \t Car number \t Owner \t Time")
            while(i<=Main_data.check_in):
                print(i,end="\t")
                for x in Main_data.security_check_in[i].keys():
                    print(Main_data.security_check_in[i][x],end="\t")
                i+=1
                print()

        elif(s_choice=="4"):
            i=1
            print("S.no \t Room number \t Name \t Car number \t Owner \t Time")
            while(i<=Main_data.check_out):
                print(i,end="\t")
                for x in Main_data.security_check_out[i].keys():
                    print(Main_data.security_check_out[i][x],end="\t")
                i+=1
                print()

        print("Enter 1 to check in a car. \nEnter 2 to ckeck out a car. \nEnter 3 to print car check in list. \nEnter 4 to print car check out list.\nEnter Exit to Exit the program")
        s_choice=input("Enter your choice") 

    print("\n\nLogging out \n\n\n")
            
                
                