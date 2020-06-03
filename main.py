import sqlite3
import random
from bikeRental import BikeRental, Customer
from time import sleep
from dbmanager import createdb, adduser, login, cu


#clear function clears the terminal output from earlier outputs
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ =system('clear')

def startshop():
    while 1 == True:
        shop = BikeRental(100)
        customer = Customer()
        print("""
            ====== Bike Rental Shop =======
            1. Display available bikes
            2. Request a bike on hourly basis $5
            3. Request a bike on daily basis $20
            4. Request a bike on weekly basis $60
            5. Return a bike
            6. Exit
            """)
            
        choice = input("Enter choice: ")
            
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            pass
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            customer.rentalTime = shop.rentBikeOnHourlyBasis(customer.requestBike())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.rentBikeOnDailyBasis(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.rentBikeOnWeeklyBasis(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            clear()
            print("""
                ====== Bike Rental Shop =======
                Thank you for using the bike rental system.
                """)
            sleep(2)
            clear()
            exit()
        else:
                print("Invalid input. Please enter number between 1-6 ")        
        

def main():
    clear()
    if path.exists('users.db') == True:
        pass
    else:
        createdb()

    while True:
        
        print("""
            ====== Bike Rental Shop =======
            1. Create user
            2. Login as exsiting user
            3. Exit
            """)
        
        option = input()
        
        try:
            option = int(option)
       
        except ValueError:
            clear()
            print("""
            ====== Bike Rental Shop =======
            That's not an int!
            """)
            sleep(2)
            clear()
            continue

        if option == 1:
            clear()
            print("""
            ====== Bike Rental Shop =======
            Enter a new user name
            """)

            username = input()


            if cu(username) == False:
                clear()
                print("""
                ====== Bike Rental Shop =======
                Username is already taken.
                Please enter another username
                """)
                sleep(2)
                clear()
                continue
            else:
                adduser(username,0,0,0,0)
                sleep(2)
                clear()
                continue
        
        if option == 2:
            clear()
            print("""
            ====== Bike Rental Shop =======
            Enter a user name
            """)

            username = input()
            if cu(username) == False:
                sleep(2)
                clear()
                startshop()
            else:
                clear()
                print("""
            ====== Bike Rental Shop =======
            Invalid username
            """)
                sleep(1)
                clear()
                main()

        if option == 3:
            clear()
            exit()
        
        else:
            clear()
            print("""
        ====== Bike Rental Shop =======
        Sorry, that is not a valid option
        """)
            sleep(2)
            clear()
            continue                   
            startshop() 

if __name__=="__main__":
    main()