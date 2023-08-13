class CoffeeMachine:
    # Constructor to initialize the initial state of the coffee machine
    def __init__(self):
        self.water = 400              # Initial amount of water
        self.milk = 540               # Initial amount of milk
        self.beans = 120              # Initial amount of coffee beans
        self.cups = 9                 # Initial number of disposable cups
        self.money = 550              # Initial amount of money
        self.water_required = 0       # Variables to store the requirements for a coffee type
        self.milk_required = 0
        self.beans_required = 0
        self.cost = 0

    # Method to display the current inventory of the coffee machine
    def inventory(self):
        print(f"""\nThe coffee machine has:
        {self.water} ml of water
        {self.milk} ml of milk
        {self.beans} g of coffee beans
        {self.cups} disposable cups
        ${self.money} of money\n""")

    # Method to handle the coffee buying process
    def buy(self, choice):
        if choice == "1":
            self.water_required = 250
            self.milk_required = 0
            self.beans_required = 16
            self.cost = 4
        elif choice == "2":
            self.water_required = 350
            self.milk_required = 75
            self.beans_required = 20
            self.cost = 7
        elif choice == "3":
            self.water_required = 200
            self.milk_required = 100
            self.beans_required = 12
            self.cost = 6
        elif choice == "back":
            return

        # Check if there are enough resources to make the selected coffee
        if (
                self.water >= self.water_required
                and self.milk >= self.milk_required
                and self.beans >= self.beans_required
                and self.cups >= 1
        ):
            print("I have enough resources, making you a coffee!\n")
            # Deduct the used resources and add money
            self.water -= self.water_required
            self.milk -= self.milk_required
            self.beans -= self.beans_required
            self.cups -= 1
            self.money += self.cost
        else:
            # Display a message if there are not enough resources
            if self.water < self.water_required:
                print("Sorry, not enough water!\n")
            elif self.milk < self.milk_required:
                print("Sorry, not enough milk!\n")
            elif self.beans < self.beans_required:
                print("Sorry, not enough coffee beans!\n")
            else:
                print("Sorry, not enough disposable cups!\n")

    # Method to handle the filling process
    def fill(self, water, milk, beans, cups):
        # Add the provided amounts to the respective resources
        self.water += water
        self.milk += milk
        self.beans += beans
        self.cups += cups

    # Method to handle the money withdrawal process
    def take(self):
        print(f"I gave you ${self.money}\n")
        self.money = 0

    # Method to interact with the user and handle user inputs
    def interact(self):
        while True:
            action = input("Write action (buy, fill, take, remaining, exit):\n> ")
            print()

            if action == "buy":
                choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n> ")
                self.buy(choice)
            elif action == "fill":
                water_added = int(input("Write how many ml of water you want to add:\n> "))
                milk_added = int(input("Write how many ml of milk you want to add:\n> "))
                beans_added = int(input("Write how many grams of coffee beans you want to add:\n> "))
                cups_added = int(input("Write how many disposable cups you want to add:\n> "))
                self.fill(water_added, milk_added, beans_added, cups_added)
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.inventory()
            else:
                break

# Create an instance of the CoffeeMachine class
coffee_machine = CoffeeMachine()
# Start the interaction with the coffee machine
coffee_machine.interact()
