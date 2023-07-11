#Use parameters to receive wash types and customer type
def carwashPrice(valuedCustomer, wash):
    #Create variables and constants for function 
    #Variable for valued customer
    valuedCustomer = valuedCustomer.upper()
    if valuedCustomer not in ["YES", "NO"]:
        raise ValueError("valuedCustomer should be either 'YES' or 'NO'")

    if wash not in [1, 2]:
        raise ValueError("wash should be either 1 or 2")

    #Basic car wash is $25
    BASIC_WASH_PRICE= 25.0
    #Super car wash is $35
    SUPER_WASH_PRICE= 35.0
    #Valued customers get 10% discount
    VALUED_CUSTOMER_DISCOUNT=0.1
    #Use if statement first and elif for the rest
    if valuedCustomer=="YES" and wash==1:
            price=BASIC_WASH_PRICE-(BASIC_WASH_PRICE*VALUED_CUSTOMER_DISCOUNT)
    elif valuedCustomer=="YES" and wash==2:
            price=SUPER_WASH_PRICE-(SUPER_WASH_PRICE*VALUED_CUSTOMER_DISCOUNT)
    elif valuedCustomer=="NO" and wash==1:
            price=BASIC_WASH_PRICE
    elif valuedCustomer=="NO" and wash==2:
            price=SUPER_WASH_PRICE
    return price

def main():
    #Welcome customer
    print("Welcome to Car Sparkle Services!")

    #Prompt customer to input whether they are a valued customer or not
    valuedCustomer=input("Are you a valued customer? Enter YES or NO: ")
    while valuedCustomer.upper()!="YES" and valuedCustomer.upper() != "NO":
          print("invalid input. Try Again.")
          valuedCustomer =input("Are you a valued customer? Enter YES or NO: ")
    
    if valuedCustomer.upper() == "YES":
          print("Hello valued customer!")
    elif valuedCustomer.upper() == "NO":
          print("Sign up to be a valued customer today for a 10% discount!")


    #Prompt user to select car wash services they need, 1 for basic, 2 for super
    wash=int(input("Select the car wash services you need. Enter 1 for Basic Wash or 2 for Super Wash: "))
    while wash != 1 and wash != 2:
          print("invalid input. Try Again.")
          wash=int(input("Select the car wash services you need. Enter 1 for Basic Wash or 2 for Super Wash: "))

    if wash == 1:
          print("You've selected Basic wash.")
    elif wash == 2:
          print("you've selected Super Wash")


    #Call carwashPrice function to calculate and return price for car wash
    washPrice=carwashPrice(valuedCustomer, wash)

    #Print car wash total price
    print("Your total price is: $",washPrice)

main()
