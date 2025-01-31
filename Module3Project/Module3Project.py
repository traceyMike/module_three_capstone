# Ice Cream Shop Application
# Author: Dr. Mary Lebens (Student Michael Tracey)
# Date 01/29/2025

# store out ice cream shop menu items
flavors = ['vanilla', 'caramel', 'mint', 'cherry', 'pecan', 'matcha'] # add three flavors more - 6 total

# add toppings options 
toppings = ['sprinkles', 'nuts', 'cherry']

# add cone type options
cones = ['cake', 'sugar', 'waffle']

# prices is dictionary - key value items pairs
# key needs to be unique - no two items with same name
prices = {"scoop": 2.50, "topping": 0.50}

# declare new function display_menu - show flavors and toppings
def display_menu():
    """show available flavors and toppings to customer"""
    print("\n=== Welcome to the Ice Cream Shop! ===")
    print("\nAvailable flavors:")

    # loop through the flavor list and show each flavor, then loop for toppings
    for flavor in flavors:
        print(f" - {flavor}")

    # print statement goes everytime there is iteration in loop
    print("\nAvailable Toppings:")
    for topping in toppings:
        print(f" - {topping}")

    # Display the prices
    # .2f for float numbers (the prices)
    print("\nPrice:")
    print(f"Scoops: ${prices['scoop']:.2f} each") # refer to scoop key (2.50)
    print(f"Toppings: ${prices['topping']:.2f} each")

def get_flavors():
    # get flavors
    # use while loop - until user is done
    chosen_flavors = []
    while True:
        try: # validate user input 
            # prompt user to choose their scoops of ice cream
            num_scoops = int(input("\nHow many scoops would you like? (1-3): "))
            # Validate the input
            if 1 <= num_scoops <= 3:
                break
            print("Please choose between 1 and 3 scoops")
        except ValueError:
            print("Please enter a number, homie!")
    # exit the while loop - stay in flavors function
    # prompt user to enter the ice cream flavor
    print("\nFor each scoop enter the flavor you like")
    for i in range(num_scoops): # i updated when loop executes
        # for loop prompts for each scoop
        # then create nested while loop - handles user input and validation
        while True: # +1 because computer starts at 0
            flavor = input(f"Scoop {i+1}: ").lower()
            # check to see if flavor is one in list
            if flavor in flavors:
                chosen_flavors.append(flavor) # add flavor using append
                break
            print("Sorry, that flavor is not available")
    # return to calling function, number of scoop user wants
    # and the flavors they picked
    # return number of scoops and chosen flavors
    return num_scoops, chosen_flavors

def get_toppings():
    """Gets topping choices from customer"""
    chosen_toppings = []

    # use while loop to prompt the user for the toppings 
    # until they are done adding toppings
    while True:
        topping = input("\nEnter a topping (or 'done' if finished): ").lower() # change topping to lowercase for uniformity
        # Test if user is done ordering toppings
        if topping == 'done':
            break
        # test if topping is in list of toppings for shop
        if topping in toppings:
            chosen_toppings.append(topping) #append topping to list
            print(f"Added {topping}!")
        else:
            print("That's too fancy player, that topping is not available")
    # return list of toppings - outside of while loop but in function
    return chosen_toppings

# create function to get the cone type from the user
def cone_type():
    print("\nChoose your cone type: (Options are cake, sugar, and waffle)")
    # loop through cone options
    for cone in cones:
        # add the f for formatting
        print(f" - {cone.title()}")
    # create while loop - prompt user
    while True:
        cone_choice = input("\nEnter your cone choice: ").lower() # lowercase
        if cone_choice in cones:
            return cone_choice # return the cone choice
        print("Sorry, we don't have that cone. Please choose sugar, waffle, cake")


def calculate_total(num_scoops, num_toppings):
    """Calculates the total cost of order"""
    scoop_cost = num_scoops * prices["scoop"] # pass key scoop
    topping_cost = num_toppings * prices["topping"] # pass key - return price
    return scoop_cost + topping_cost # return total

def print_receipt(num_scoops, chosen_flavors, chosen_toppings, cone_choice):
    """Prints a nice receipt for the customer"""
    print("\n== Your Ice Cream Order ===")
    print(f"Cone Type: {cone_choice.title()}") # show the cone choice

    for i in range(num_scoops):
        print(f"Scoop {i+1}: {chosen_flavors[i].title()}") # .title for first letter capital [i] start at 0

    if chosen_toppings:
        print("\nToppings:")
        # Loop through list of toppings
        for topping in chosen_toppings:
            print(f" - {topping.title()}")
    
    # print the total - call calculate_total function pass it num_scoops and len method
    total = calculate_total(num_scoops, len(chosen_toppings))
    print(f"\nTotal: ${total:.2f}")

    # Save order to file - record of ice cream sold
    with open("daily_orders.txt", "a") as file:
        file.write(f"\nOrder: {num_scoops} scoops in a {cone_choice} - ${total:.2f}")

# Main function acts as automatic function
# defined a main function - then it is ran first before other functions
def main():
    display_menu() # call display menu - add functions in order of what you want to be called
    # calling get_flavors - returns number of scoops & list of flavors
    num_scoops, chosen_flavors = get_flavors()
    # call get_toppings - returns list of toppings
    chosen_toppings = get_toppings()
    # get cone type from user
    cone_choice = cone_type()
    # Display the receipts
    print_receipt(num_scoops, chosen_flavors, chosen_toppings)


# this line automatically executes main when app runs 
if __name__ == "__main__":
    main()