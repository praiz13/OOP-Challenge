from pet import Pet

def main():
    name = input("🐶 Name your pet: ")
    my_pet = Pet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed 🥣")
        print("2. Sleep 😴")
        print("3. Play 🎾")
        print("4. Status 📊")
        print("5. Train a Trick 🎓")
        print("6. Show Tricks 🤹‍♂️")
        print("7. Quit ❌")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            my_pet.get_status()
        elif choice == "5":
            trick = input("Enter a trick to teach your pet: ")
            my_pet.train(trick)
        elif choice == "6":
            my_pet.show_tricks()
        elif choice == "7":
            print(f"Goodbye! {my_pet.name} will miss you! 🐾")
            break
        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
