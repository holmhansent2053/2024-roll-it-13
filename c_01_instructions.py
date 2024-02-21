print("🎲🎲 roll it 13 🎲🎲")

# loop for testing purposes

while True:
    want_instructions = input("Do you want to read the instructions? ")

    if want_instructions == "yes":
        print("you chose yes")
    elif want_instructions == "no":
        print("you chose no")

    else:
        print("You did not choose a valid response")
want_instructions = yes_no("Do you want to read the instructions?")
print(f"You chose {want_instructions}")

