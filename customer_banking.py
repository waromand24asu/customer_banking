# Import the create_cd_account and create_savings_account functions
from Account import Account
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_account = Account(balance=0, interest=0)
    print()
    savings_account.balance = float(input("Enter the Savings account balance: "))
    savings_account.interest = float(input("Enter the Savings account annual interest rate: "))
    savings_account.months = int(input("Enter, in months, how long funds will be held in the savingsaccount: "))

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned_savings = create_savings_account(savings_account.balance, savings_account.interest, savings_account.months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print()
    print(f"Interest earned on savings: {interest_earned_savings:.2f}")
    print(f"Updated savings balance: {updated_savings_balance:.2f}")
    print()

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_account = Account(balance=0, interest=0)
    cd_account.balance = float(input("Enter the CD account balance: "))
    cd_account.interest = float(input("Enter the CD account interest rate: "))
    cd_account.months = int(input("Enter, in months, how long funds will be held in the CD account: "))


    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned_cd = create_cd_account(cd_account.balance, cd_account.interest, cd_account.months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print()
    print(f"Interest earned: {interest_earned_cd:.2f}")
    print(f"Updated savings balance: {updated_cd_balance:.2f}")
    print()

if __name__ == "__main__":
    # Call the main function.
    main()
