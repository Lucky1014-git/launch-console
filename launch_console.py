
name = input("What's your name? ")
print("Welcome, {name}!")
running = True
while running:
    print("1: About me")
    print("2: My goals")
    print("3: Fun Fact")
    print("4: Exit")
    choice = input("Pick 1-4: ")
    if choice == "1":
        print("I'm a senior at Rouse High School!")
    elif choice == "2":
        print("My goal is to ship my first real project!")
    elif choice == "3":
      print("One fun fact about me is that I have been playing the piano for 12+ years!")
    elif choice == "4":
        print("Goodbye!")
        running = False
    else:
        print("Please pick 1, 2, or 3.")
