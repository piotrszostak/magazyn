
items = [
    {'name': 'kurtka',
     'quantity': 3,
     'unit': 'pcs',
     'unit_price': 300},
    {'name': 'bluza',
     'quantity': 5,
     'unit': 'pcs',
     'unit_price': 200},
    {'name': 'koszulka',
     'quantity': 13,
     'unit': 'pcs',
     'unit_price': 50}
]

def list_items():
    print(items)
    
def get_items():
    print("Name\tQuantity\tUnit\tUnit Price (PLN)")
    for item in items:
        #TODO
        print(item['name'] +'\t'+ str(item['quantity']) +'\t'+item['unit'] +'\t'+ str(item['unit_price']))

def menu():
    while True:
        user_input = input("What would you like to do? (show, list, exit)\n")
        
        if user_input == 'list':
            list_items()
        elif user_input == 'show':
            get_items()
        elif user_input == 'exit':
            exit()
        else:
            continue

menu()

