
items = [
    {'name': 'kurtka',
     'quantity': 3,
     'unit': 'pcs',
     'unit_price': 300},
    {'name': 'bluza',
     'quantity': 5,
     'unit': 'pcs',
     'unit_price': 200},
    {'name': 't-shirt',
     'quantity': 13,
     'unit': 'pcs',
     'unit_price': 50}
]

def list_items():
    print(items)
    
def show():
    print("{:<8} {:<8} {:<8} {:<16}".format("Name", "Quantity", "Unit", "Unit Price (PLN)"))
    print("{:<8} {:<8} {:<8} {:<16}".format("----", "--------", "----", "----------------"))
    for item in items:
        print("{:<8} {:<8} {:<8} {:<16}".format(item['name'], item['quantity'], item['unit'], item['unit_price']))
def menu():
    while True:
        user_input = input("What would you like to do? (show, list, exit)\n")
        
        if user_input == 'list':
            list_items()
        elif user_input == 'show':
            show()
        elif user_input == 'exit':
            print("Exiting...")
            exit()
        else:
            continue

menu()

