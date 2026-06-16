# Voting System

votes = {
    "A": 0,
    "B": 0,
    "C": 0
}

is_running = True

while is_running:
    print("\n===== Voting System =====")
    print("1. Vote")
    print("2. Show Results")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nCandidates:")
        print("A")
        print("B")
        print("C")

        candidate = input("Vote for a candidate: ").upper()

        if candidate in votes:
            votes[candidate] += 1
            print("Vote recorded successfully!")
        else:
            print("Invalid candidate!")

    elif choice == "2":
        print("\n===== Results =====")
        for candidate, vote_count in votes.items():
            print(f"{candidate}: {vote_count} votes")

    elif choice == "3":
        print("Voting Closed!")
        is_running = False

    else:
        print("Invalid Choice!")
