# Get input from user
answer=input("What is the answer to the Great Question of Life, the Universe and Everything? ").strip()

# Print Yes if the user inputs 42 or (case-insesitively) forty-two or forty two

if answer=="42":
    print("Yes")
elif answer.lower()=="forty-two":
    print("Yes")
elif answer.lower()=="forty two":
    print("Yes")
else:
    print("No")