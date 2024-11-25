# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and uppercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for NOn-alphabetical or invalid entries.


def check_letter():
    # Your control flow logic goes here
    letter = input("Enter a letter: ")
    if letter.isalpha() == False:
        print("Invalid input. Please enter a letter.")
    elif letter.upper() in ["a", "e", "i", "o", "u"]:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")


# Call the function
check_letter()
print("----------------------------------")
# Exercise 2: Old eNOugh to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old eNOugh to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (NO negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.


def check_voting_eligibility():
    # Your control flow logic goes here
    age = input("Please enter your age: ")
    if int(age) < 0:
        print("invalid unput. please enter a valid age.")
    elif int(age) < 18:
        print("You are NOt eligible to vote.")
    else:
        print("You are eligible to vote.")

        # print("Invalid input. Please enter a valid age.")


# Call the function
check_voting_eligibility()
print("----------------------------------")
# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.


def calculate_dog_years():
    # Your control flow logic goes here
    dog_age = input("Input a dog's age: ")
    dog_age = int(dog_age)
    if dog_age < 0:
        print("Invalid input. Please enter a valid age.")
    elif dog_age <= 2:
        dog_years = dog_age * 10
    else:
        dog_years = (dog_age - 2) * 7 + 20

    print(f"The dog's age in dog years is {dog_years}.")


# Call the function
calculate_dog_years()
print("----------------------------------")
# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (YES/NO).
# - Then, ask if it is raining (YES/NO).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.


def weather_advice():
    # Your control flow logic goes here
    cold = input("Is it cold? (YES/NO): ")
    raining = input("Is it raining? (YES/NO): ")

    if cold.upper() == "YES" and raining.upper() == "YES":
        print("Wear a waterproof coat.")
    elif cold.upper() == "YES" and raining.upper() == "NO":
        print("Wear a warm coat.")
    elif cold.upper() == "NO" and raining.upper() == "YES":
        print("Carry an umbrella.")
    else:
        print("Wear light clothing.")


# Call the function
weather_advice()
print("----------------------------------")
# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.


def determine_season():
    # Your control flow logic goes here
    month = input("Enter the month of the year (Jan - Dec): ")
    day = int(input("Enter the day of the month: "))

    if month.upper() not in [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]:
        print("Invalid input. Please enter a valid month.")
    elif day < 1 or day > 31:
        print("Invalid input. Please enter a valid day.")
    else:
        if (
            (month.upper() == "DEC" and day >= 21)
            or (month.upper() == "JAN")
            or (month.upper() == "FEB")
            or (month.upper() == "MAR" and day < 20)
        ):
            season = "Winter"
        elif (
            (month.upper() == "MAR" and day >= 20)
            or (month.upper() == "APR")
            or (month.upper() == "MAY")
            or (month.upper() == "JUN" and day < 21)
        ):
            season = "Spring"
        elif (
            (month.upper() == "JUN" and day >= 21)
            or (month.upper() == "JUL")
            or (month.upper() == "AUG")
            or (month.upper() == "SEP" and day < 22)
        ):
            season = "Summer"
        else:
            season = "Fall"

        print(f"{month} {day} is in {season}.")


# Call the function
determine_season()
