# Create a Budget class that can instantiate objects based on different budget categories like food, clothing,
# and entertainment. These objects should allow for depositing and withdrawing funds from each category,
# as well computing category balances and transferring balance amounts between categories.

# The user can determine if he wants to access his budget to view (Then which one)or add to it (add to which one or
# take from which to which) or withdraw ( subtract from which and how much and to which)
def transactions_read():
    with open('budget_sheet.txt', 'r') as f:
        lines = [line.rstrip() for line in f]
        print(lines)


def transactions_update():
    infile = open("Transactions.txt", "w")
    for i in listOfTrans:
        infile.write(f"{i}\n")
    infile.close()


class Budget:

    def __init__(self, initial_balance=0.0):
        self.from_account = None
        self.to_account = None  # MOVE
        self.category = None
        self.amount = initial_balance
        self._clothing = initial_balance
        self._entertainment = initial_balance
        self._food = initial_balance
        self._cat = initial_balance
        self._balance = initial_balance

    def add(self, category, amount):
        self.category = None
        self.amount = int(amount)
        self.category = category
        listOfCat = ["Food", "Entertainment", "Clothing"]

        if self.category == listOfCat[0]:
            self._food = self._food + self.amount
            print(f"The balance of {category} now stands at {self._food}")
            new = f"You have added ${self._food} dollars to the {category} category"
            listOfTrans.append(new)

            return self._food
        if self.category == listOfCat[1]:
            self._entertainment = self._entertainment + self.amount
            print(f"The balance of {category} now stands at {self._entertainment}")
            new = f"You have added ${self._entertainment} dollars to the {category} category"
            listOfTrans.append(new)

            return self._entertainment

        if self.category == listOfCat[2]:
            self._clothing = self._clothing + self.amount
            print(f"The balance of {category} now stands at {self._clothing}")
            new = f"You have added ${self._clothing} dollars to the {category} category"
            listOfTrans.append(new)

            return self._clothing

    def withdraw(self, from_account, to_account):
        global money_account_from, money_account_to
        self.from_account = from_account
        self.to_account = to_account
        withdraw_amount = self.withdraw_amount_val(self.from_account)

        listOfCat = ["Food", "Entertainment", "Clothing"]
        if self.from_account == listOfCat[0]:
            money_account_from = self._food
            self._food = money_account_from
            money_account_from = money_account_from - withdraw_amount
            new = f"You withdrew ${withdraw_amount} dollars from the {self.from_account} category"
            listOfTrans.append(new)
        if self.from_account == listOfCat[1]:
            money_account_from = self._entertainment
            money_account_from = money_account_from - withdraw_amount
            self._entertainment = money_account_from
            new = f"You withdrew ${withdraw_amount} dollars from the {self.from_account} category"
            listOfTrans.append(new)
        if self.from_account == listOfCat[2]:
            money_account_from = self._clothing
            money_account_from = money_account_from - withdraw_amount
            self._clothing = money_account_from
            new = f"You withdrew ${withdraw_amount} dollars from the {self.from_account} category"
            listOfTrans.append(new)

        if self.to_account == listOfCat[0]:
            money_account_to = self._food
            money_account_to = money_account_to + withdraw_amount
            self._food = money_account_to
            new = f"You have added ${withdraw_amount} dollars to the {self.to_account} category"
            listOfTrans.append(new)
        if self.to_account == listOfCat[1]:
            money_account_to = self._entertainment
            money_account_to = money_account_to + withdraw_amount
            self._entertainment = money_account_to
            new = f"You have added ${withdraw_amount} dollars to the {self.to_account} category"
            listOfTrans.append(new)
        if self.to_account == listOfCat[2]:
            money_account_to = self._clothing
            money_account_to = money_account_to + withdraw_amount
            self._clothing = money_account_to
            new = f"You have added ${withdraw_amount} dollars to the {self.to_account} category"
            listOfTrans.append(new)
        print(f"The balance of the {self.from_account} stands at ${money_account_from}")
        print(f"The balance of the {self.to_account} stands at ${money_account_to}")

    def withdraw_amount_val(self, category):
        global money
        listOfCat = ["Food", "Entertainment", "Clothing"]
        if category == listOfCat[0]:
            money = self._food
        if category == listOfCat[1]:
            money = self._entertainment
        if category == listOfCat[2]:
            money = self._clothing
        print(f"The balance of the {category} stand at ${money}")
        with_draw_amount = input("Enter the amount you want to withdraw : $")
        try:
            with_draw_amount = int(with_draw_amount)
        except ValueError:
            print("Invalid input!")
            with_draw_amount = input("Enter the amount you want to withdraw: $")
        finally:

            return with_draw_amount

    def view(self, numOfChoice):
        # listOfDisplays = ["all", "Food", "Entertainment", "Clothing"]
        # self.balance_read()
        if numOfChoice == 1:
            print("%-15s   %10s" % ("The Category", "The Balance"))
            print("%-15s | %10d$" % ("Food", self._food))
            print("%-15s | %10d$" % ("Entertainment", self._entertainment))
            print("%-15s | %10d$" % ("Clothing", self._clothing))
        if numOfChoice == 2:
            print(f"The balance of the food budget now stands at ${self._food}")
        if numOfChoice == 3:
            print(f"The balance of the Entertainment budget now stands at ${self._food}")
        if numOfChoice == 4:
            print(f"The balance of the Clothing budget now stands at ${self._food}")

    def balance_update(self):
        infile = open("budget_sheet.txt", "w")
        infile.write(f"{self._food}\n")
        infile.write(f"{self._entertainment}\n")
        infile.write(f"{self._clothing}\n")
        infile.close()

    def balance_read(self):
        with open('budget_sheet.txt', 'r') as f:
            lines = [line.rstrip() for line in f]
            self._food = lines[0]
            self._entertainment = lines[1]
            self._clothing = lines[2]
            self._food = int(self._food)
            self._entertainment = int(self._entertainment)
            self._clothing = int(self._clothing)


def validate(x):
    if x.isspace():
        return False
    if x.isdigit():
        return False
    if not (x == "v" or x == "a" or x == "w"):
        return False
    return True


def category_input_proper():
    the_cat = input("Enter the category you want to add to: ")
    the_cat = the_cat[0].upper() + the_cat[1:].lower()
    return the_cat


def view_input():
    print(" [1 = All,2 = Food, 3 = Entertainment, 4 = Clothing]")
    the_view = input("Enter the category you want to view: ")
    the_view = int(the_view)
    return the_view


def amount_input_proper():
    the_amount = input("Enter the amount you want to add to the category: $")
    try:
        the_amount = int(the_amount)
    except ValueError:
        print("Invalid input!")
        the_amount = input("Enter the amount you want to add to the category: $ ")
    finally:
        return the_amount


def from_account_val():
    from_account = input("Enter the category you want to withdraw from: ")
    from_account = from_account[0].upper() + from_account[1:].lower()
    return from_account


def to_account_val():
    to_account = input("Enter the category you want to add the money to: ")
    to_account = to_account[0].upper() + to_account[1:].lower()
    return to_account


money = 0
money_account_from = ""
money_account_to = ""
listOfTrans = []


def main():
    objectA = Budget()
    objectA.balance_read()
    firstInput = input("Enter 'v' to view or 'a' to add or 'w' to withdraw or 't' to view transactions: ")
    while firstInput != " ":
        if validate(firstInput):
            if firstInput == "a":
                objectA.add(category_input_proper(), amount_input_proper())
            elif firstInput == "v":
                objectA.view(view_input())
            elif firstInput == "w":
                objectA.withdraw(from_account_val(), to_account_val())
            elif firstInput == "t":
                objectA.transactions_read()
        elif firstInput == "":
            print("The program will stop now...")
            objectA.balance_update()
            objectA.transactions_update()
            break
        firstInput = input("Enter 'v' to view or 'a' to add or 'w' to withdraw or 't' to view transactions: ")


main()
