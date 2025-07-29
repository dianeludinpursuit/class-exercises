# This is a simple Python script that first prints "Hello World!",
# then asks for the user's name, verifies it through a confirmation step,
# and finally prints a personalized greeting. It includes a special
# welcome message for a specific name and adds further interactive elements.

def hello_world():
  """
  First prints "Hello World!", then asks the user for their name,
  confirms it, and then engages in a more personalized information exchange.
  The script waits for the user to type their name before proceeding to verification.
  """
  # Print the initial "Hello World!" phrase
  print("Hello World!")

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

  # Check if the confirmed user_name is "Diane Ludin" (case-insensitive)
  if user_name.lower() == "diane ludin":
    print("Hey, it's the awesome AI Director, Diane Ludin!")
  else:
    # For any other name, print the regular personalized greeting.
    print(f"Hello, {user_name}!")

  print("\nLet's get to know each other a little more!")

  # --- New interactive conditions start here ---

  # Ask for favorite color and respond based on the input
  favorite_color = input("What's your favorite color? ").lower().strip()
  if "blue" in favorite_color:
    print("Ah, blue! The color of the sky and the ocean. A very calming choice.")
  elif "red" in favorite_color:
    print("Red, a color of passion and energy! I like it!")
  elif "green" in favorite_color:
    print("Green, representing nature and growth. Wonderful!")
  else:
    print(f"That's a lovely color, {user_name}!")

  # Ask for a simple "how are you" and respond based on mood
  mood = input("How are you feeling today (e.g., good, tired, excited)? ").lower().strip()
  if "good" in mood or "great" in mood or "happy" in mood:
    print("That's fantastic to hear! Keep up the positive vibes.")
  elif "tired" in mood:
    print("Oh, I understand. Make sure to get some rest!")
  elif "excited" in mood:
    print("Excitement is contagious! What's got you so pumped?")
  else:
    print("Thanks for sharing. I hope your day goes well!")

  print("\nThis was a great little chat!")


# Call the function to execute the script when the script is run directly.
if __name__ == "__main__":
  hello_world()
