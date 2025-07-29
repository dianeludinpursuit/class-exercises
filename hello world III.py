# This is a simple Python script that asks for the user's name,
# verifies it through a confirmation step, and then prints a personalized greeting.

def hello_world():
  """
  Asks the user for their name, confirms it, and then prints a personalized "Hello" message.
  The script waits for the user to type their name before proceeding to verification.
  """
  user_name = ""
  name_confirmed = False

  # Loop to ensure the name is correctly entered and confirmed by the user
  while not name_confirmed:
    # Prompt the user to enter their name. The script will wait here until
    # the user types their name and presses Enter.
    user_name = input("What's your name? ")

    # After the user types their name, move onto the verification part.
    # Ask the user to confirm the entered name.
    confirmation = input(f"You entered '{user_name}'. Is this correct? (yes/no): ").lower().strip()

    if confirmation == "yes":
      name_confirmed = True
      print("Great! Confirmed.")
    elif confirmation == "no":
      # If the name is not correct, the loop will re-prompt for the name.
      print("No problem, let's try again.")
    else:
      # Handle invalid input for the confirmation step.
      print("Invalid input. Please type 'yes' or 'no'.")

  # Once the verification steps have been completed by the user and the script,
  # print a thank you message including the user's name.
  print(f"Thank you, {user_name}!")

  # Finally, print the personalized greeting using the confirmed name.
  print(f"Hello, {user_name}!")

# Call the function to execute the script when the script is run directly.
if __name__ == "__main__":
  hello_world()
