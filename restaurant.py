import Main_data

def print_menu():
    print("Item \t price")
    for x in Main_data.food_menu.keys():
        print(x,Main_data.food_menu[x],sep="\t")


def food_order(g_room):
    price=0
    order=[]
    print_menu()
    item=input("Enter Exit to Exit \nEnter the item name you want to order")
    while(item!="Exit"):
        if(item not in Main_data.food_menu.keys()):
            print("Item not in the list")
            continue
        order.append(item)
        price+=Main_data.food_menu[item]
        item=input("Enter the item name you want to order")
    
    print("Your order list id",order)
    print("Total Bill is",price)
    return (price)