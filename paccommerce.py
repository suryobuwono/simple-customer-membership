from tabulate import tabulate
from math import sqrt


class Membership:

    benefit = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Discount": ["15%", "10%", "8%"],
        "Another Benefit": ["Silver & Gold Benefits + Holiday Vouchers + Cashback up to 30%",
                            "Silver Benefits + Online Ride Voucher", "Meal Voucher"]
    }

    registered_member = {
        "Sumbul": "Platinum",
        "Ana": "Gold",
        "Cahya": "Platinum"
    }
    requirements = {
        "Membership": ["Platinum", "Gold", "Silver"],
        "Monthly Expense (million)": [8, 6, 5],
        "Monthly Income (million)": [15, 10, 7]
    }

    def __init__(self, username: str):
        self.monthly_expense = None
        self.monthly_income = None
        self.membership = None
        """
        Verifies whether a user with the same name in the database is a duplicate
        with a different identity or is a valid re-entry of the same identity.
        """
        if username in Membership.registered_member.keys():
            print(f"To verify your identity as {username}, please answer:")
            membership = input(f" - Your membership type = ")
            password = input(f" - Your user password = ")
            if membership == Membership.registered_member[username] and password == "registered_member":
                self.membership = membership
                print(" ")
                print(f"Welcome back, {username}! Thank you for verifying your identity.")
            else:
                raise RuntimeError(f"You are not {username}. Please choose another username.")
        self.username = username


    def show_benefit(self):
        """Displays the benefits of all membership tiers."""
        benefit_table = tabulate(Membership.benefit, headers="keys")
        print("PacCommerce Membership Benefits")
        print(" ")
        print(benefit_table)


    def show_requirements(self):
        """Displays the monthly income and expense requirements for each membership."""
        requirements_table = tabulate(Membership.requirements, headers="keys")
        print("PacCommerce Membership Requirements")
        print(" ")
        print(requirements_table)


    def predict_membership(self, monthly_expense: int, monthly_income: int):
        """
        Predicts membership based on the lowest Euclidean distance to requirements.

        Parameters:
            - monthly_expense (int): User's monthly expenses.
            - monthly_income (int): User's monthly income.

        Output:
            - Displays Euclidean distance results for each membership tier.
            - Updates self.membership with the closest matching tier.
            - Adds user to the registered members database.
        """
        self.monthly_expense = monthly_expense
        self.monthly_income = monthly_income

        # Calculate euclidean distance and store the results into a dictionary
        e_distance = {}
        constant = list(Membership.requirements.values())

        for i in range(len(constant[0])):
            tier = constant[0][i]
            req_expense = constant[1][i]
            req_income = constant[2][i]
            d = sqrt((monthly_expense - req_expense)**2 + (monthly_income - req_income)**2)
            e_distance[tier] = round(d, 2)

        # Sort and take the smallest distance value, assign the key to self.membership
        lowest_distance = sorted(e_distance.items(), key=lambda x: x[1])
        self.membership = lowest_distance[0][0]

        # Insert username and membership to the registered members database
        if self.username in Membership.registered_member.keys():
            Membership.registered_member[self.username] = self.membership
        else:
            Membership.registered_member.update({self.username: self.membership})

        print(f"Euclidean Distance calculation for user {self.username}: {e_distance}")
        print(" ")
        print("Based on the result, you have been automatically registered as a member of:")
        return self.membership


    def show_membership(self):
        """Displays the user's current membership, if already predicted."""
        if self.membership == None:
            print(f"User {self.username} is not yet a member. Please run 'predict_membership' first.")
        else:
            print(f"User {self.username} is currently a {self.membership} Member.")


    def __show_all_members(self):
        """
        Private method to display all registered members, used internally by:
            - show_all_members()
            - remove_member()

        Purpose:
            To protect user data, access to view or delete members is restricted
            to authorized users only.

            This method centralizes the display logic to avoid code redundancy.
        """
        name = Membership.registered_member.keys()
        membership = Membership.registered_member.values()

        row = [[n, m] for n, m in zip(name, membership)]
        header = ["Name", "Membership"]
        table = tabulate(row, headers=header)
        print(table)


    def show_all_members(self):
        """Displays all registered members (authorized users only)."""
        # Authorization is done by matching the password input
        password = input("Enter admin password: ")

        if password == "pacmann":
            print("Access granted. Displaying all registered members.")
            print(" ")
            self.__show_all_members()
        else:
            raise RuntimeError("Incorrect password. You are not authorized to view registered members.")


    def remove_member(self, username: str):
        """Removes a member (authorized users only)."""
        if username not in Membership.registered_member.keys():
            raise NameError(f"Username '{username}' is not registered as a PacCommerce member.")

        # Authorization is done by matching the password input
        password = input("Enter admin password: ")

        if password == "pacmann":
            print(f"Access granted. User '{username}' has been removed.")
            Membership.registered_member.pop(username)
            print(" ")
            print("Updated registered members list:")
            self.__show_all_members()
        else:
            raise RuntimeError("Incorrect password. You are not authorized to remove members.")


    def calculate_price(self, price_list: list):
        """
        Calculates total shopping cost with membership discounts.

        Parameters:
            - price_list (list): List of item prices for this purchase.

        Rules:
            - Platinum → 15% discount
            - Gold → 10% discount
            - Silver → 8% discount

        Output:
            - Displays the net total after discount for the current user.
        """
        discount = {
            tier: int(disc.replace("%","")) / 100 for tier, disc
            in zip(Membership.benefit["Membership"], Membership.benefit["Discount"])
        }
        gross = sum(price_list)
        cut_price = gross * discount[self.membership]
        nett = gross - cut_price

        print(f"Congratulations! You received a membership discount of {Membership.format_rupiah(cut_price)} in this transaction.")
        print(" ")
        print(f"Total amount payable by user {self.username} is:")
        print(f"{Membership.format_rupiah(nett)}")


    @staticmethod
    def format_rupiah(amount):
        """
        Format a number into Indonesian Rupiah format.
        Example: 120000 -> 'Rp 120.000,00'
        """
        formatted = f"{amount:,.2f}"
        formatted = formatted.replace(",","X").replace(".",",").replace("X",".")
        return f"Rp {formatted}"