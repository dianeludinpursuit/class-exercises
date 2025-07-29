# This is a simple Python script that asks for the user's name and prints a personalized greeting.

def hello_world():
  """
  Asks the user for their name and then prints a personalized "Hello" message.
  """
  # Prompt the user to enter their name
  user_name = input("What's your name? ")

  # Print a personalized greeting
  print(f"Hello, {user_name}!")

# Call the function to execute the script.
if __name__ == "__main__":
  hello_world()
