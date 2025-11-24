import Admin
import Login_credentials_data as credentials
import reception
import Security as Secutiry
import customers
import room_service

def program():
    print("Enter 1 to proceed. \nEnter Exit to exit")
    choice=input("Enter the choice")
    
    while(choice!="Exit"):
        fl=True
        userid=input("Enter the user id")
        password=input("Enter the password")
        if((userid==credentials.admin_userid and password==credentials.admin_password)):
            fl=False
            Admin.admin()
            
        for x in credentials.reception_credentials.keys():
            if((userid==credentials.reception_credentials[x]["userid"] and password==credentials.reception_credentials[x]["Password"])):
                fl=False
                reception.Reception()
                
        for x in credentials.security_credentials.keys():
            if((userid==credentials.security_credentials[x]["userid"] and password==credentials.security_credentials[x]["Password"])):
                fl=False
                Secutiry.program()
                
        for x in credentials.cleaning_credentials.keys():
            if((userid==credentials.cleaning_credentials[x]["userid"] and password==credentials.cleaning_credentials[x]["Password"])):
                fl=False
                room_service.program()
        if((userid in int(credentials.room_password) ) and (password==credentials.room_password[userid])):
            fl=False
            customers.program()
        
        if(fl):
            print("Invalid credentials")
        choice=input("Enter the choice of the Log In Page")