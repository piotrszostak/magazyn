def menu():
    while True:
        user_input = input("What would you like to do?\n")
        
        if user_input == '':
            #func1()
            pass
        elif user_input == 'exit':
            exit()
        else:
            continue

menu()

items = [
    {name: kurtka,
     quantity: 3,
     unit: pcs,
     unit_price: 300},
    {name: bluza,
     quantity: 5,
     unit: pcs,
     unit_price: 200},
    {name: koszulka,
     quantity: 13,
     unit: pcs,
     unit_price: 50}
]