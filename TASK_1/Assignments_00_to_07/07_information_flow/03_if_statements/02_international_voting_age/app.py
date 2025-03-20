# Defining the minimum voting ages for three fictional countries
VOTING_AGE_A = 16  # Country A (e.g., NeoLand)
VOTING_AGE_B = 25  # Country B (e.g., Eldoria)
VOTING_AGE_C = 48  # Country C (e.g., Grayshore)

def check_voting_eligibility():
    """
    Asks the user for their age and checks if they are eligible to vote
    in three different fictional countries.
    """
    # Taking user input and converting it to an integer
    user_age = int(input("Enter your age: "))

    # Checking voting eligibility for Country A
    if user_age >= VOTING_AGE_A:
        print(f"You can vote in NeoLand where the voting age is {VOTING_AGE_A}.")
    else:
        print(f"You cannot vote in NeoLand where the voting age is {VOTING_AGE_A}.")

    # Checking voting eligibility for Country B
    if user_age >= VOTING_AGE_B:
        print(f"You can vote in Eldoria where the voting age is {VOTING_AGE_B}.")
    else:
        print(f"You cannot vote in Eldoria where the voting age is {VOTING_AGE_B}.")

    # Checking voting eligibility for Country C
    if user_age >= VOTING_AGE_C:
        print(f"You can vote in Grayshore where the voting age is {VOTING_AGE_C}.")
    else:
        print(f"You cannot vote in Grayshore where the voting age is {VOTING_AGE_C}.")

# Running the function only when the script is executed directly
if __name__ == "__main__":
    check_voting_eligibility()
